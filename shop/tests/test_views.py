from django.test import TestCase, Client
from shop.models import Product
from shop.views import PurchaseCreate

class PurchaseCreateTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        Product.objects.create(name="table", price="2000")

    def test_webpage_accessibility(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_buy_webpage(self):
        response = self.client.get('/buy/1/')
        self.assertEqual(response.status_code, 200)

    def test_buy_function(self):
        response = self.client.post('/buy/1/', {'product': '3',
                                               'price': '0',
                                               'person': 'Кирилл',
                                               'address': 'Невская 99',
                                               'birthday': '2023-01-12'})
        self.assertEqual(response.status_code, 200)