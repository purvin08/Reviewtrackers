import unittest
import requests

from webscrape import search_url


class ApiTest(unittest.TestCase):
    api_url = "http://127.10.0.0:9000/"

    def test_get_all_reviews(self):
        r = requests.get(search_url)
        self.assertEqual(r.status_code, 200)
