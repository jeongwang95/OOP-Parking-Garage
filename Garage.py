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

# my_garage = Garage(10)
# my_garage.take_ticket()
# print(my_garage.tickets)
# print(my_garage.current_ticket)


    def pay_for_parking(self):

        ticket_no = int(input(" what is your ticket number? :"))

        if ticket_no in self.current_ticket:
            print(f"Your ticket number {ticket_no} costs $20.")
            response = input("Would you like to pay for your ticket now? Enter y/n: ")

            if response.lower().strip() in ('y','yes'):
                self.current_ticket[ticket_no] = 0
                print("Thank you for paying your ticket, please exit garage within 15 mins.")
            else:
                print("Okay! Please pay before you exit the garage.")
            
        else:
            print(f"{ticket_no} is not valid. Please double check your {ticket_no}.")

        
    

        
