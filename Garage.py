import time
class Member():
    def __init__(self, name, plate_num, cc):
        self.name = name
        self.plate_num = plate_num
        self.cc = cc
        self.active = True

    # change membership status
    def togle_membership(self):
        if self.active:
            self.active = False
            print("Your membership is no longer active.")
        else:
            self.active = True
            print("Welcome back! Your credit card on file has been charged.")
    
    # change credit card in account. example of use: when cc expired user can update their payment with a new cc
    def change_cc(self, new_cc):
        self.cc = new_cc
        print("The credit card on your account has been updated!")


class Garage():
    def __init__(self, parking_spaces):
        self.parking_spaces = parking_spaces
        self.taken_spaces = 0
        self.tickets = [x for x in range(1, self.parking_spaces + 1)]
        self.current_ticket = {}
        self.members = []

    def take_ticket(self, member = False):
        if self.parking_spaces - self.taken_spaces == 0:
            print('Sorry! Parking Garage is full!')
        else:
            # if the user is a JKT member, set enter time to 0 since they do not have to pay for parking
            if member:
                ticket_no = self.tickets.pop(0)
                self.current_ticket[ticket_no] = 0
                self.taken_spaces += 1
                print(f'Here is your ticket. Your ticket number is {ticket_no}')
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
                if parking_fee == 1:
                    print("Your vehicle has been towed. Please contact the garage manager to get the towing info.")
                else:
                    print(f"Your parking fee is ${parking_fee}")
                
                response = input("Would you like to pay for your ticket now? Enter y/n: ")
                
                if response.lower().strip() in ('y','yes'):
                    self.current_ticket[ticket_no] = time.time() # when the ticket has been paid, replace the enter time with the paid ticket time
                    print("Thank you for paying your ticket, please exit garage within 15 mins. Failing to exit within 15 mins will incur extra charges.")
                else:
                    print("Okay! Please pay before you exit the garage.")           
        else:
            print(f"Ticket number {ticket_no} is not valid. Please double check your ticket number.")

    def leave_garage(self):
        end_time = time.time() # need to calculate the end time again to make sure people are leaving within the 15 min exit window
        ticket_no = int(input("What is your ticket number? "))

        # check if ticket number is in our current ticket dict
        if ticket_no in self.current_ticket:
            # ticket has been paid for and is leaving within the 15 min exit time 
            # or the vehicle stay has been less than 15 mins
            # or is the vehicle is a JKT parking member
            if end_time - self.current_ticket[ticket_no] <= 15 or self.current_ticket[ticket_no] == 0:
                print("Thank you for using our parking garage. Have a nice day!")
                self.taken_spaces -= 1
                del self.current_ticket[ticket_no]
                self.tickets.append(ticket_no)

            # ticket has not been paid
            else:
                print("Your ticket was not paid for. Please pay your ticket before leaving the garage.")
                print("If you paid for your ticket and still got charged, that means your 15 min exit time has expired, so you have to pay for extra time.")
        else:
            print(f"Ticket number {ticket_no} is not valid. Please double check your ticket number.")

    def ticket_price_calc(self, duration):
        if duration <= 15:
            return 0
        elif duration > 15 and duration < 60:
            return 5
        elif duration >= 60 and duration <= 180:
            return 20
        elif duration > 180 and duration <= 360:
            return 50
        elif duration > 360 and duration <= 1440:
            return 70
        else:
            return 1

    def display_rates(self):
        print("""
Garage Rates:

First 15 mins:      FREE
16-60 mins:         $5
61-180 mins:        $20
181-360 mins:       $50
361-1440 mins:      $70
1440+ mins:         Vehicle Towed
        """)
            
class Main:
    def run():
        my_garage = Garage(10)

        while True:
            print("\nWelcome to JKT Short Term Parking Garage!")
            print("IMPORTANT: IF VEHICLE STAYS OVER 24HRS, IT WILL BE TOWED!")
            print("""
Main Menu:

[A] View Garage Rates
[B] Take a ticket
[C] Pay for your ticket
[D] Leave Garage
[E] JKT Member Check-In/Join membership
[F] Exit application

            """)
            response = input("Please choose from the options above: ")
            if response.lower().strip() == 'a':
                my_garage.display_rates()
            elif response.lower().strip() == 'b':
                my_garage.take_ticket()
            elif response.lower().strip() == 'c':
                my_garage.pay_for_parking()
            elif response.lower().strip() == 'd':
                my_garage.leave_garage()
            elif response.lower().strip() == 'e': # Goes to membership menu
                while True:
                    print("""
JKT Members Menu:

[A] Enter Garage/Account Manager
[B] Join JKT Parking Membership
[C] Return to Main Menu
                    """)
                    decision = input("Please choose from the options above: ")
                    if decision.lower().strip() in ('c', 'q', 'quit'):
                        break
                    # add new member into members list
                    elif decision.lower().strip() in ('b', 'join', 'new'):
                        print("Thank you for your interest in joining JTK Parking memebership.")
                        print("The membership cost $200 per month. The membership comes with unlimited parking while the membership is active.")
                        response = input("Are you still interested in joining? ('y','n') ")
                        if response.lower().strip() in ('n', 'no', 'q', 'quit'):
                            print("No worries. You can still park as a guest! Exiting to main menu.")
                            break
                        elif response.lower().strip() in ('y', 'yes', 'yea', 'yeah'):
                            name = input("What is your name? ")
                            plate_num = input("Input license plate number: ")
                            while True: # make sure users input valid cc number
                                cc = input("Input credit card number to make payment: ")
                                if len(cc) == 16 and isinstance(int(cc), int):
                                    break
                                else:
                                    print("Invalid cc number please try again. When inputing cc number do not put spaces in between numbers.")
                            my_garage.members.append(Member(name.title().strip(), plate_num.lower().strip(), cc))
                            print("Congratulations! You are now member of JKT Parking. Please input your license plate number in the JKT members menu to enter the garage.")
                        else:
                            print('Invalid input. Please try again.')
                    # Goes to account manager where members can enter garage, change membership or cc
                    elif decision.lower().strip() == 'a':
                        num = input("Please input your license plate number: ") # license plate # used to check membership
                        for member in my_garage.members:
                            # license plate has been found so the user is a member of JKT. now the program goes to account manager menu
                            if num.lower().strip() == member.plate_num:
                                while True:
                                    print(f"Hello {member.name}! What would you like to do?")
                                    print("""
[A] Enter Garage
[B] Change Credit Card
[C] Change Membership
[D] Return to Previous Menu                                  
                                    """)
                                    choice = input("Choose from the options above: ")
                                    if choice.lower().strip() in ('d', 'q', 'quit', 'return', 'back'):
                                        break
                                    elif choice.lower().strip() == 'c':
                                        member.togle_membership()
                                    elif choice.lower().strip() == 'b':
                                        while True: # make sure users input valid cc number
                                            new_cc = input("Input credit card number to make payment: ")
                                            if len(new_cc) == 16 and isinstance(int(new_cc), int):
                                                break
                                            else:
                                                print("Invalid cc number please try again. When inputing cc number do not put spaces in between numbers.")
                                        member.change_cc(new_cc)
                                    elif choice.lower().strip() in ('a', 'enter'):
                                        if member.active:
                                            my_garage.take_ticket(True)
                                            break
                                        else:
                                            print("Oh no! Your membership is currently not active. Please reactivate your membership before entering the garage.")
                                    else:
                                        print('Invalid input. Please try again.')
                        else:
                            print(f"{num} is not a member. Please double check your license plate number.")
                    else: 
                        print('Invalid input. Please try again.')
                        
            elif response.lower().strip() == 'f':
                break
            else:
                print('Invalid input. Please try again.')

Main.run()


        
    

        
