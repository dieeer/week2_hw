from numpy import number

from classes.song import Song

class Room:
    def __init__(self, room_number, till, entry_fee):
        self.room_number = room_number
        self.till = till
        self.entry_fee = entry_fee
        self.guests_in_room = []
        self.songs_in_queue = []

    def add_guest(self, guest_to_add):
        self.guests_in_room.append(guest_to_add)

    def remove_guest(self, guest_to_remove):
        self.guests_in_room.remove(guest_to_remove)

    def increase_till(self, addition):
        self.till += addition

    def add_song(self, song_to_add):
        self.songs_in_queue.append(song_to_add)

    def get_current_song(self):
        return self.songs_in_queue

    def check_in_to_room(self, guest_to_add, room, song):
        # if guest_to_add.sufficient_funds(): 
        guest_to_add.reduce_wallet(5.0)
        room.increase_till(5.0)
        room.add_song(song)