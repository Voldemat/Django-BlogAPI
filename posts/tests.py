from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post
from modules import ModelTestCase
# Create your tests here.
data = {
			'title':'title',
			'body':'body',
			'author':get_user_model().objects.get(id = 1)
		}
class PostTestCase(ModelTestCase, TestCase):
	def setUp(self):
		self.create_model(Post, data)

	def test_content(self):
		self.check_content_of_model()