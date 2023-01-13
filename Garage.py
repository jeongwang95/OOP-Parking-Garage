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

    
    # pay for parking method
    def pay_for_parking(self):

        # user inputs their parking ticket number
        ticket_no = int(input("What is your ticket number? "))

        # if the parking ticket number is in our current parking tickets
        if ticket_no in self.current_ticket:
            # check if the ticket has already been paid for
            if self.current_ticket[ticket_no] == 0:
                print("Your ticket has already been paid for. Please proceed to leave the garage.")
            
            # if the ticket hasnt been paid yet, calculate parking fee
            else:
                end_time = time.time()
                duration = end_time - self.current_ticket[ticket_no]
                print(f"Ticket number: {ticket_no}\nYou have been in the garage for {int(duration)} mins.")
                
                parking_fee = self.ticket_price_calc(duration)
                if parking_fee == 0:
                    print("Your vehicle has been towed. Please contact the garage manager to get the towing info.")
                else:
                    print(f"Your parking fee is ${parking_fee}")
                
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

    def ticket_price_calc(self, duration):
        if duration < 60:
            return 5
        elif duration >= 60 and duration <= 180:
            return 20
        elif duration > 180 and duration <= 360:
            return 50
        elif duration > 360 and duration <= 1440:
            return 70
        else:
            return 0

    def display_rates(self):
        print("""
Garage Rates:

Less than 60 mins:  $5
61-180 mins:        $20
181-360 mins:       $50
361-1440 mins:      $70
1440+ mins:         Vehicle Towed
        """)
            
class Main:
    def run():
        my_garage = Garage(10)

        while True:
            print("Welcome to JKT Short Term Parking Garage!")
            print("IMPORTANT: IF VEHICLE STAYS OVER 24HRS, IT WILL BE TOWED!")
            print("""
Please choose from the options below:

[A] View Garage Rates
[B] Take a ticket
[C] Pay for your ticket
[D] Leave Garage
[E] Exit application

            """)
            response = input("Option: ")
            if response.lower().strip() == 'a':
                my_garage.display_rates()
            elif response.lower().strip() == 'b':
                my_garage.take_ticket()
            elif response.lower().strip() == 'c':
                my_garage.pay_for_parking()
            elif response.lower().strip() == 'd':
                my_garage.leave_garage()
            elif response.lower().strip() == 'e':
                break
            else:
                print('Invalid input. Please try again.')

Main.run()


        
    

        
