from django.test import TestCase
from django.contrib.auth.models import User
from weather.models import SearchHistory


class SearchHistoryModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',
                                             password='testpassword')

    def test_create_search_history(self):
        history = SearchHistory.objects.create(user=self.user, city='Berlin')
        self.assertEqual(history.user, self.user)
        self.assertEqual(history.city, 'Berlin')

    def test_search_history_str(self):
        history = SearchHistory.objects.create(user=self.user, city='Berlin')
        self.assertEqual(str(history), 'Berlin searched by testuser')
