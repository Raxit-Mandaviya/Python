# Class & Object(Instance of a class)
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
            
    def start(self):
        print(f"{self.make} {self.model} is starting")
    
    def stop(self):
        print(f"{self.make} {self.model} is stopping")

my_car = Car(
    make="Toyota",
    model="Corolla",
    year="2019",
)

# Accessing class attributes
print(my_car.make)
print(my_car.model)
print(my_car.year)

# Accessing class methods

# Create an instance of the Car class
my_car = Car("Toyota", "Camry", 2021)

# Call and print the start and stop methods
my_car.start()
my_car.stop()


# Inheritance

class Vehical: # Parent class
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Bike(Vehical): # Child class inheriting from Vehical
    def speak(self):
        return f"{self.name} sounds Wroom Wroom!"

class Car(Vehical): # Another child class inheriting from Vehical
    def speak(self):
        return f"{self.name} sounds Wroooooooom!"

# Creating objects of each class
vehical = Vehical("All vehicals")
bike = Bike("Bike")
car = Car("Car")

# Calling the speak method on each object
print(vehical.speak())  # Output from parent class
print(bike.speak())     # Output from Dog class
print(car.speak())     # Output from Cat class

# Encapsulation

class BankAccount:
    def __init__(self, account_number, balance, account_type, account_holder_name):
        self.account_number = account_number  # Public attribute
        self.account_type = account_type      # Public attribute
        self.__account_holder_name = account_holder_name  # Private attribute
        self.__balance = balance  # Private attribute (note the double underscore)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return f"Current balance: {self.__balance}"
    
    def get_account_holder_name(self):
        return f"Account holder: {self.__account_holder_name}"

account = BankAccount("2303031087008", 10000, "Savings", "Rakshit Mandaviya") # Create an instance of BankAccount

# Accessing public attributes
print(f"Account Number: {account.account_number}")
print(f"Account Type: {account.account_type}")

# Accessing private attribute using the public method
print(account.get_account_holder_name())  
print(account.get_balance())  

# Trying to access private attribute directly (not recommended)
# print(account.__account_holder_name)  # This will raise an AttributeError

# Perform deposit and withdraw operations
account.deposit(500)
account.withdraw(300)
print(account.get_balance())


# Polymorphism

class Dog:
    def speak(self):
        return "Dog barks!"

class Cat:
    def speak(self):
        return "Cat Meows!"

class Cow:
    def speak(self):
        return "Cow Moos!"

animals = [Dog(), Cat(), Cow()]  # Makes instances of all classes

for animal in animals:
    print(animal.speak())  # Calls only one speak() method to return all classes

# Method Overriding

class Animal:
    def speak(self):
        return "Animal speaks!"
    
class Dog(Animal):
    def speak(self):
        return "Dog barks!"
    
class Cat(Animal):
    def speak(self):
        return "Cat meows!"
    
class Cow(Animal):
    def speak(self):
        return "Cow moos!"
    
animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(animal.speak())

# Method Overloading

class Calculator:
    def add(self, a, b, c=None):
        if c:
            return a + b + c
        else:
            return a + b
        
calculator = Calculator()
print(calculator.add(2, 2))
