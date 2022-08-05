import unittest
from classes.room import Room
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(101)
        self.guest = Guest("dave")

    def test_room_has_number(self):
        self.assertEqual(101, self.room.room_number)

    def test_add_guest(self):
        self.room.add_guest(self.guest)
        self.assertEqual(1, len(self.room.guests_in_room))

    def test_remove_guest(self):
        self.room.add_guest(self.guest)
        self.room.remove_guest(self.guest)
        self.assertEqual(0, len(self.room.guests_in_room))
    
    