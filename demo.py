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



# encapsulation :
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

# Creating an object of the BankAccount class
account = BankAccount(1000)

# Accessing private attribute using public method
print(account.get_balance())  # Output: 1000



# inheritance :
class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):  # Car class inherits from Vehicle
    def drive(self):
        print("Car is driving")

my_car = Car()
my_car.start()  # Inherited method
my_car.drive()  # Method of Car class




# polymorphism :
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

animals = [Dog(), Cat()]
for animal in animals:
    animal.speak()  # Calls the speak method specific to each class


# Abstraction :
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

circle = Circle(5)
print(circle.area())  # Output: 78.5