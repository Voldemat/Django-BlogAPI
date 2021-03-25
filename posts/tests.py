from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post
# from modules import ModelTestCase
# Create your tests here.

class PostTestCase(TestCase):
	@classmethod
	def setUpTestData(cls):
		testuser1 = get_user_model().objects.create_user(
			username = 'testuser1',
			password = 'abc123'
		)
		testuser1.save()
		test_post = Post.objects.create(
			author 	= testuser1,
			title	= 'Blog title',
			body	= 'Body content...' 
		)
		test_post.save()

	def test_blog_content(self):
		post = Post.objects.get(id = 1)
		author = str(post.author)
		title = str(post.title)
		body = str(post.body)
		self.assertEqual(author, 'testuser1')
		self.assertEqual(title, 'Blog title')
		self.assertEqual(body, 'Body content...')