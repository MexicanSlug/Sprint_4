import unittest
from api.order import Order
from api.ice_storm import IceStorm
from api.food import Food
from api.drink import Drink

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.order = Order()

    def test_add_ice_storm(self):
        storm = IceStorm("Chocolate")
        storm.add_topping("Cherry")
        self.order.add_item(storm)
        self.assertEqual(self.order.get_num_items(), 1)

    def test_add_food(self):
        fries = Food("French Fries")
        fries.add_topping("Ketchup")
        self.order.add_item(fries)
        self.assertEqual(self.order.get_num_items(), 1)

    def test_add_drink(self):
        soda = Drink("Sbrite", "Large")
        soda.add_flavor("Cherry")
        self.order.add_item(soda)
        self.assertEqual(self.order.get_num_items(), 1)

    def test_receipt(self):
        storm = IceStorm("Vanilla Bean")
        storm.add_topping("Pecans")
        fries = Food("French Fries")
        fries.add_topping("Cheese")
        soda = Drink("Sbrite", "Medium")
        soda.add_flavor("Lime")
        self.order.add_item(storm)
        self.order.add_item(fries)
        self.order.add_item(soda)
        receipt = self.order.get_receipt()
        self.assertEqual(len(receipt["items"]), 3)
        self.assertAlmostEqual(receipt["subtotal"], storm.get_total() + fries.get_total() + soda.get_total())

if __name__ == "__main__":
    unittest.main()
