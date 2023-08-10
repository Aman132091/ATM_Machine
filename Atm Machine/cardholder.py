# class cardHolder ():
#     def __init__(self, cardNum ,pin, firstname, lastname, balance):
#         self.cardNum = cardNum
#         self.pin =pin
#         self.firstname=firstname
#         self.lastname=lastname
#         self.balance=balance
        
#         ###Getter method
#         def get_cardNum(self):
#             return self.cardNum
#         def get_pin(self):
#             return self.pin
#         def get_firstname(self):
#             return self.firstname
#         def get_lastname(self):
#             return self.lastname
#         def get_balance(self):
#             return self.balance
        
#         ###setter method

#         def set_cardNum(self, newval):
#             self.cardNum=newval
#         def set_pin(self, newval):
#             self.pin=newval
#         def set_firstname(self, newval):
#             self.firstname=newval
#         def set_lastname(self, newval):
#             self.lastname=newval
#         def set_balance(self, newval):
#             self.balance=newval


#         def print_out(self):
#             print("card #: ", self.cardNum)
#             print("pin #: ", self.pin)
#             print("firstname #: ", self.firstname)
#             print("lastname #: ", self.lastname)
#             print("balance #: ", self.balance)

class cardHolder():
    def __init__(self, cardNum, pin, firstname, lastname, balance):
        self.cardNum = cardNum
        self.pin = pin
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance

    # Getter methods
    def get_cardNum(self):
        return self.cardNum

    def get_pin(self):
        return self.pin

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def get_balance(self):
        return self.balance

    # Setter methods
    def set_cardNum(self, newval):
        self.cardNum = newval

    def set_pin(self, newval):
        self.pin = newval

    def set_firstname(self, newval):
        self.firstname = newval

    def set_lastname(self, newval):
        self.lastname = newval

    def set_balance(self, newval):
        self.balance = newval

    def print_out(self):
        print("card #: ", self.cardNum)
        print("pin #: ", self.pin)
        print("firstname #: ", self.firstname)
        print("lastname #: ", self.lastname)
        print("balance #: ", self.balance)
