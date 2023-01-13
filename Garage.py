import time
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
            ticket_no = self.tickets.pop(0)
            self.current_ticket[ticket_no] = time.time()
            self.taken_spaces += 1
            print(f'Here is your ticket. Your ticket number is {ticket_no}')

    def pay_for_parking(self):

        ticket_no = int(input("What is your ticket number? "))

        if ticket_no in self.current_ticket:
            if self.current_ticket[ticket_no] == 0:
                print("Your ticket has already been paid for.")
            else:
                end_time = time.time()
                duration = end_time - self.current_ticket[ticket_no]
                print(f"Ticket number: {ticket_no}\nYou have been in the garage for {int(duration)} mins. Your parking fee is $20")
                response = input("Would you like to pay for your ticket now? Enter y/n: ")

                if response.lower().strip() in ('y','yes'):
                    self.current_ticket[ticket_no] = 0
                    print("Thank you for paying your ticket, please exit garage within 15 mins.")
                else:
                    print("Okay! Please pay before you exit the garage.")           
        else:
            print(f"Ticket number {ticket_no} is not valid. Please double check your ticket number.")

    def leave_garage(self):
        ticket_no = int(input("What is your ticket number? "))

        # check if ticket number is in our current ticket dict
        if ticket_no in self.current_ticket:
            # ticket has been paid for
            if self.current_ticket[ticket_no] == 0:
                print("Thank you for using our parking garage. Have a nice day!")
                self.taken_spaces -= 1
                del self.current_ticket[ticket_no]
                self.tickets.append(ticket_no)

            # ticket has not been paid
            else:
                print("Your ticket was not paid for. Please pay your ticket before leaving the garage.")
        else:
            print(f"Ticket number {ticket_no} is not valid. Please double check your ticket number.")
            
class Main:
    def run():
        my_garage = Garage(10)

        while True:
            print("Welcome to JKT Garage! Please choose from the options below:")
            print("""

[1] Take a ticket
[2] Pay for your ticket
[3] Leave Garage
[4] Exit application

            """)
            response = input("Option: ")
            if response.lower().strip() == '1':
                my_garage.take_ticket()
            elif response.lower().strip() == '2':
                my_garage.pay_for_parking()
            elif response.lower().strip() == '3':
                my_garage.leave_garage()
            elif response.lower().strip() == '4':
                break
            else:
                print('Invalid input. Please try again.')

Main.run()


        
    

        
