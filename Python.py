# Python Notes
# Python Cheat Sheet: https://www.pythonsheets.com/notes/python-tests.html

############# Variables ##############
name = "John"
age = 20

############## Console ##############

# Console Operations
print("Hello World!")
name = input("What is your name? ")

############## List, Dictionary, Tuple, Set ##############

# List Types
names = list()  # Empty List
names = ["John", "Mary", "Bob"]  # Normal List

# List Operations
names.append("John")  # Add to list
names.remove("John")  # Remove from list
names.pop(0)  # Remove from list by index
names.clear()  # Clear list
names.sort()  # Sort list
names.reverse()  # Reverse list
names.count("John")  # Count items in list
names.index("John")  # Get index of item in list
names.copy()  # Copy list


# Tuple Types. What is a tuple? A tuple is a list that cannot be changed. It is immutable.
names = tuple()  # Empty Tuple
names = ("John", "Mary", "Bob")  # Normal Tuple


# Set Types. What is a set? A set is a list that cannot have duplicates.
names = set()  # Empty Set
names = {"John", "Mary", "Bob"}  # Normal Set


# Dictionary Types
person = dict()  # Empty Dictionary
person = {"name": "John", "age": 20}  # Normal Dictionary

############## Operators ##############

# Arithmetic Operators
print(10 + 3)  # Addition
print(10 - 3)  # Subtraction
print(10 * 3)  # Multiplication
print(10 / 3)  # Division
print(10 // 3)  # Division without remainder
print(10 % 3)  # Remainder
print(10**3)  # Exponent

# Comparison Operators
print(10 > 3)  # Greater than
print(10 >= 3)  # Greater than or equal to
print(10 < 3)  # Less than
print(10 <= 3)  # Less than or equal to
print(10 == 3)  # Equal to
print(10 != 3)  # Not equal to

# Logical Operators
print(10 > 3 and 10 < 20)  # And
print(10 > 3 or 10 < 20)  # Or
print(not 10 > 3)  # Not

# Identity Operators
print(10 is 10)  # Is
print(10 is not 10)  # Is not

# Membership Operators
print("John" in ["John", "Mary", "Bob"])  # In
print("John" not in ["John", "Mary", "Bob"])  # Not in

############## SLICE OPERATOR ##############

# Slice Operator
numbers = [1, 2, 3, 4, 5]
#                      [start:end:step]
print(numbers[0:3])  # [1, 2, 3] # start at index 0 and go to index 3
print(numbers[:3])  #  [1, 2, 3] # start at the beginning and go to index 3
print(numbers[1:])  #  [2, 3, 4, 5] # start at index 1 and go to the end
print(numbers[:])  #  [1, 2, 3, 4, 5] # start at the beginning and go to the end
print(
    numbers[::2]
)  #  [1, 3, 5] # start at the beginning and go to the end by stepping 2


############## IF ELSE ##############

# If Statements
if name == "John":
    print("Hello John!")
elif name == "Mary":
    print("Hello Mary!")
else:
    print("Hello Stranger!")


############## Loops ##############

# For Loops
for i in range(0, 10):
    print(i)

# For Loops with step
#        range(start, end, step)
for i in range(0, 10, 2):
    print(i)

# Loops with Lists
names = ["John", "Mary", "Bob"]
for name in names:
    print(name)

# Loops with Dictionaries
person = {"name": "John", "age": 20}
for key, value in person.items():
    print(key, value)

# Loops with enumerate
names = ["John", "Mary", "Bob"]
for index, name in enumerate(names):
    print(index, name)

# While Loops
i = 0
while i < 10:
    print(i)
    i += 1


############## Functions ##############


# Functions
def say_hello(name):
    print("Hello " + name)


# Functions with overloading
def say_hello(name, age):
    print("Hello " + name + " you are " + str(age))


# Functions with default values
def say_hello(name, age=20):
    print("Hello " + name + " you are " + str(age))


############## Classes ##############


# Classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello " + self.name + " you are " + str(self.age))


# Classes with inheritance
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def say_hello(self):
        super().say_hello()
        print("Your student id is " + str(self.student_id))


############## Files ##############

# Read File
file = open("file.txt", "r")  # r = read
content = file.read()
file.close()

# Write File

file = open("file.txt", "w")  # w = write
file.write("Hello World!")
file.close()

# Append File

file = open("file.txt", "a")  # a = append
file.write("Hello World!")
file.close()

############## Modules ##############

# Importing Modules
import math

print(math.sqrt(16))

# Importing Modules with alias
import math as m

# Importing specific functions from a module
from math import sqrt

print(sqrt(16))

# Importing specific functions from a module with alias
from math import sqrt as s

print(s(16))

# Importing everything from a module
from math import *

print(sqrt(16))


############## Exceptions ##############

# Try Catch
try:
    print(10 / 0)
except ZeroDivisionError:
    print("You cannot divide by zero")

# Try Catch with finally
try:
    print(10 / 0)
except ZeroDivisionError:
    print("You cannot divide by zero")
finally:
    print("This will always be executed")

# Try Catch with multiple exceptions
try:
    print(10 / 0)
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("You cannot convert a string to a number")

# Try Catch with multiple exceptions with alias
try:
    print(10 / 0)
except (ZeroDivisionError, ValueError) as error:
    print(error)
