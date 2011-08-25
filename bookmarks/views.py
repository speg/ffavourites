# Create your views here.
from bookmarks.models import *
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User

'''
To fetch users who have bookmarks x,y,z:
User.objects.filter(userprofile__bookmarks__title__contains='mine')

This gets user objects, who have user profiles that have bookmarks that have title...

'''

def index(request):
	from django.db.models import Count
	new_bookmarks = Bookmark.objects.all().order_by('-pk')[:5]
	logged_in = True if request.user.is_authenticated() else False
	#your five latest bookmarks
	yours = request.user.get_profile().bookmarks.all().order_by('-pk')[:5] if logged_in else None	
	popular = UserBookmarked.objects.values('bookmark__id','bookmark__title','bookmark__url').annotate(dcount=Count('bookmark__id')).order_by('-dcount')[:5]
	
	for i in popular:
		print i['bookmark__title']
	
	return render_to_response('bookmarks/index.html',
	{	'newest':new_bookmarks,
		'logged_in':logged_in,
		'name':request.user.username,
		'yours':yours,
		'popular':popular	
	})

@csrf_protect
def register(request):
	from django.contrib.auth.forms import UserCreationForm
	from django.template import RequestContext
	from django.contrib.auth import authenticate, login
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			name = form.clean_username()
			passw = form.clean_password2()
			form.save()
			user = authenticate(username=name,password=passw)
			login(request,user)
			return HttpResponseRedirect(reverse('bookmarks.views.index'))
	return render_to_response('registration/create.html',
		{	'form':UserCreationForm(),
		},
		context_instance=RequestContext(request))

def add(request):
	from bookmarks.models import UserBookmarked
	#strip out http://
	url = request.GET['url'][7:] if request.GET['url'][:7]=='http://' else request.GET['url']
	#get or create bookmark
	obj, created = Bookmark.objects.get_or_create(title=request.GET['title'], url=url)
	#add to user's profile
	ub = UserBookmarked.objects.get_or_create(user=request.user.get_profile(),bookmark=obj)
	#ub.save()
	
	return HttpResponseRedirect(reverse('bookmarks.views.index'))
	#return HttpResponse('Saved!')