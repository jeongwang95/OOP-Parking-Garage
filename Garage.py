class Garage():
    def __init__(self, parking_spaces):
        self.parking_spaces = parking_spaces
        self.taken_spaces = 0
        self.tickets = [x for x in range(1, self.parking_spaces + 1)]
        self.current_ticket = {}

    def take_ticket(self):
        if self.parking_spaces - self.taken_spaces == 0:
            print('Sorry! Parking Garage is full!')
        else:
            self.current_ticket[self.tickets.pop(0)] = 20
            self.taken_spaces += 1
            print('Here is your ticket.')

my_garage = Garage(10)
my_garage.take_ticket()
print(my_garage.tickets)
print(my_garage.current_ticket)
