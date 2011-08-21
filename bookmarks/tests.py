from django.utils import unittest
from models import Bookmark

class MyFuncTestCase(unittest.TestCase):
	
	def testTwo(self):
		b = Bookmark(title='title',url='url')
		b.save()
		self.assertEqual(b.pk,1)
		self.assertEqual(b.title,'title')
		