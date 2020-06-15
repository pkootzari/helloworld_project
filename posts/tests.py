from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text="just a tesst")

    def test_text_content(self):
        post = Post.objects.get(id = 1)
        name = f'{post.text}'
        self.assertEqual(name, 'just a tesst')

class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='this is another test')
    
    def test_view_url(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_template(self):
        resp = self.client.get(reverse('home'))
        self.assertTemplateUsed(resp, 'home.html')
        