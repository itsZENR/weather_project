from django.test import SimpleTestCase
from django.urls import reverse, resolve
from weather.views import index, autocomplete, history


class UrlsTest(SimpleTestCase):
    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    def test_autocomplete_url_is_resolved(self):
        url = reverse('autocomplete')
        self.assertEqual(resolve(url).func, autocomplete)

    def test_history_url_is_resolved(self):
        url = reverse('history')
        self.assertEqual(resolve(url).func, history)
