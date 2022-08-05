import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(101, 100.00, 5.0)
        self.guest = Guest("dave", 40.0)
        self.song = Song("Love Lost", "Mac Miller")

    def test_room_has_number(self):
        self.assertEqual(101, self.room.room_number)

    def test_room_has_till(self):
        self.assertEqual(100.00, self.room.till)

    def test_room_has_entry_fee(self):
        self.assertEqual(5.0, self.room.entry_fee)

    def test_increase_till(self):
        self.room.increase_till(5.0)
        self.assertEqual(105.00, self.room.till)

    def test_add_guest(self):
        self.room.add_guest(self.guest)
        self.assertEqual(1, len(self.room.guests_in_room))

    def test_remove_guest(self):
        self.room.add_guest(self.guest)
        self.room.remove_guest(self.guest)
        self.assertEqual(0, len(self.room.guests_in_room))

    def test_add_song(self):
        self.room.add_song(self.song)
        self.assertEqual(1, len(self.room.songs_in_queue))
    
    def test_get_current_song(self):
        self.room.add_song(self.song)
        self.room.get_current_song()
        self.assertEqual("Love Lost", self.song.song_name)

    # def test_check_in(self):
    #     self.assertEqual(35.0, self.guest.wallet)
    #     self.assertEqual(105.0, self.room.till)
    #     self.room.get_current_song()
    #     self.assertEqual("Love Lost", self.song.song_name)