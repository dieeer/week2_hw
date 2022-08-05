import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Lost Love", "Mac Miller")
    
    def test_song_has_name(self):
        self.assertEqual("Lost Love", self.song.song_name)
    
    def test_song_has_artist(self):
        self.assertEqual("Mac Miller", self.song.artist)
        