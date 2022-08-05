import unittest
from classes.guest import Guest
from classes.room import Room

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.room = Room(101, 100.00, 5.0)
        self.guest = Guest("dave", 40.0)

    def test_guest_has_name(self):
        self.assertEqual("dave", self.guest.guest_name)

    def test_guest_has_wallet(self):
        self.assertEqual(40.0, self.guest.wallet)
    
    # def test_sufficient_funds(self):
    #     self.assertEqual(True, self.guest.sufficient_funds(self.room.entry_fee))

    def test_reduce_wallet(self):
        self.guest.reduce_wallet(5)
        self.assertEqual(35.0, self.guest.wallet)

    # def test_charge_entry(self):
    #     self.guest.charge_entry(self.guest)
    #     self.assertEqual(35.0, self.guest.wallet)