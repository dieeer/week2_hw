from numpy import number


class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.guests_in_room = []

    def add_guest(self, guest_to_add):
        self.guests_in_room.append(guest_to_add)

    def remove_guest(self, guest_to_remove):
        self.guests_in_room.remove(guest_to_remove)
