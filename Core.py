# Core Python Concepts

# 1. Variables and Data Types
x = 10          # Integer
y = 3.14        # Float
name = "Alice"  # String
is_active = True  # Boolean

# 2. Lists
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Accessing list element
print(fruits[2])  # Accessing list element
print(fruits[1])  # Accessing list element

# 3. Tuples
coordinates = (10, 20)
print(coordinates[1])  # Accessing tuple element

# 4. Dictionaries
person = {"name": "Alice", "age": 25}
print(person["name"])  # Accessing dictionary value
print(person["age"])  # Accessing dictionary value

# 5. Conditional Statements
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

# 6. Loops
# For loop
for fruit in fruits:
    print(fruit)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# 7. Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Bob"))

# 8. Classes and Objects
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"

my_dog = Dog("Buddy", 3)
print(my_dog.name)
print(my_dog.bark())

# 9. Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# 10. File Handling
with open("example.txt", "w") as file:
    file.write("Hello, World!")