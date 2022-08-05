from classes.room import Room

class Guest:
    def __init__(self, guest_name, wallet):
        self.guest_name = guest_name
        self.wallet = wallet

    def reduce_wallet(self, subtraction):
        self.wallet -= subtraction

    def sufficient_funds(self, room):
        return self.wallet >= room.entry_fee

    # def charge_entry(self, room):
    #     if self.sufficient_funds():
    #         self.reduce_wallet(room)
