from django.test import TestCase
from .models import Order, Data
import datetime

# Create your tests here.
class OrderModelTest(TestCase):
    def setUp(self):
      self.newOrder = Order(invoice_no='76d456',
                            stock_code='123',
                            description='test description',
                            quantity=3,
                            invoice_date=datetime.datetime.now(),
                            unit_price=4.5,
                            customerID=109,
                            country='Kenya'
                            )
    def test_order_instance(self):
      self.assertTrue(isinstance(self.newOrder, Order))
    
    def test_to_string_method(self):
      self.assertEqual(str(self.newOrder), '76d456 - test description')


