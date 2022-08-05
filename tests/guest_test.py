import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("dave")

    def test_guest_has_name(self):
        self.assertEqual("dave", self.guest.guest_name)