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

detail = student("sanoj",'arunachalam nagar',8939120547)
detail.inform()



# Defining a class
class Car:
    def __init__(self, color, model):
        self.color = color  # Attribute
        self.model = model  # Attribute

    def drive(self):  # Method
        print(f"The {self.color} {self.model} is driving.")

# Creating an object of the Car class
my_car = Car("red", "Toyota")  # Object of class Car

# Accessing object attributes and methods
print(my_car.color)  # Output: red
my_car.drive()       # Output: The red Toyota is driving.