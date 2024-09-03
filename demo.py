#oops concept :


# this  is class and object assigned:

class student :
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number

    def inform(self):
        print("this is" ,self.name)
        print("his address",self.address)
        print("his phone number",self.phone_number)

detail = student("sanoj",'arunachalam nagar',8939100547)
detail.inform()