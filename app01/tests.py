from django.test import TestCase

# Create your tests here.
class SomeBasicTest(TestCase):
    def test_text_correct(self):
        response = self.client.get('/')
        self.assertIn('Welcome', response)
