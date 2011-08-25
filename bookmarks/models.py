from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Bookmark(models.Model):
	title = models.CharField(max_length=256)
	url = models.CharField(max_length=256)	
	
	def __unicode__(self):
		return '%s (%d)' % (self.title,self.id)

class UserProfile(models.Model):
	# This field is required.
	user = models.OneToOneField(User)
	# Other fields here
	bookmarks = models.ManyToManyField(Bookmark,through='UserBookmarked')
	
	def __unicode__(self):
		return self.user.username

class UserBookmarked(models.Model):
	user = models.ForeignKey(UserProfile)
	bookmark = models.ForeignKey(Bookmark)
	liked = models.BooleanField(default=False)
	
	def __unicode__(self):
		return '%s | %s (%d)' % (self.user.user.username,self.bookmark.title,self.bookmark.id)
	
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)		