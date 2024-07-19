from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from weather.models import SearchHistory


class WeatherViewsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser',
                                             password='testpassword')

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'weather/index.html')

    def test_get_weather(self):
        response = self.client.get(reverse('index'), {'city': 'Berlin'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Прогноз погоды для Berlin')

    def test_autocomplete(self):
        response = self.client.get(reverse('autocomplete'), {'term': 'Ber'})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            ['Berlin']
        )

    def test_history_view_logged_in(self):
        self.client.login(username='testuser', password='testpassword')
        SearchHistory.objects.create(user=self.user, city='Berlin')
        response = self.client.get(reverse('history'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'weather/history.html')
        self.assertContains(response, 'Berlin')

    def test_history_view_not_logged_in(self):
        response = self.client.get(reverse('history'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/history/')