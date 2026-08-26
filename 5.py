# ============================================================
#              PYTHON LONG PRACTICE PROGRAM
# ============================================================

import random
import math
from datetime import datetime


# ============================================================
# 1. BASIC VARIABLES
# ============================================================

name = "Rahul"
age = 20
city = "Lucknow"
marks = 87.5
is_student = True

print("Name:", name)
print("Age:", age)
print("City:", city)
print("Marks:", marks)
print("Student:", is_student)


# ============================================================
# 2. STRING PRACTICE
# ============================================================

first_name = "Rahul"
last_name = "Kumar"

full_name = first_name + " " + last_name

print("\nFull Name:", full_name)
print("Upper:", full_name.upper())
print("Lower:", full_name.lower())
print("Title:", full_name.title())
print("Length:", len(full_name))

if "Rahul" in full_name:
    print("Rahul is present in the name.")

print("First character:", full_name[0])
print("Last character:", full_name[-1])


# ============================================================
# 3. USER INPUT
# ============================================================

print("\n--- User Input ---")

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

print("Hello", user_name)
print("You are", user_age, "years old.")

if user_age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# ============================================================
# 4. BASIC CALCULATOR
# ============================================================

print("\n--- Calculator ---")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

if b != 0:
    print("Division:", a / b)
    print("Floor Division:", a // b)
    print("Remainder:", a % b)
else:
    print("Cannot divide by zero.")

print("Power:", a ** b)


# ============================================================
# 5. IF / ELIF / ELSE
# ============================================================

print("\n--- Grade Calculator ---")

score = float(input("Enter your score: "))

if score >= 90:
    grade = "A+"
elif score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
elif score >= 50:
    grade = "D"
else:
    grade = "F"

print("Your grade is:", grade)


# ============================================================
# 6. FOR LOOP
# ============================================================

print("\n--- Numbers 1 to 20 ---")

for i in range(1, 21):
    print(i)


# ============================================================
# 7. EVEN AND ODD
# ============================================================

print("\n--- Even and Odd Numbers ---")

for i in range(1, 31):

    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")


# ============================================================
# 8. MULTIPLICATION TABLE
# ============================================================

print("\n--- Multiplication Table ---")

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# ============================================================
# 9. SUM OF NUMBERS
# ============================================================

print("\n--- Sum of Numbers ---")

total = 0

for i in range(1, 101):
    total += i

print("Sum from 1 to 100:", total)


# ============================================================
# 10. FACTORIAL
# ============================================================

print("\n--- Factorial ---")

number = int(input("Enter a number for factorial: "))

factorial = 1

if number < 0:
    print("Factorial does not exist for negative numbers.")
else:

    for i in range(1, number + 1):
        factorial *= i

    print("Factorial:", factorial)


# ============================================================
# 11. WHILE LOOP
# ============================================================

print("\n--- While Loop ---")

count = 1

while count <= 10:
    print("Count:", count)
    count += 1


# ============================================================
# 12. LIST PRACTICE
# ============================================================

print("\n--- List Practice ---")

fruits = [
    "Apple",
    "Banana",
    "Mango",
    "Orange",
    "Grapes"
]

print("Fruits:", fruits)

fruits.append("Watermelon")
fruits.insert(1, "Papaya")

print("After adding:", fruits)

fruits.remove("Banana")

print("After removing Banana:", fruits)

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

print("Total fruits:", len(fruits))

print("\nAll fruits:")

for fruit in fruits:
    print("-", fruit)


# ============================================================
# 13. LIST OPERATIONS
# ============================================================

numbers = [12, 5, 89, 34, 21, 67, 2, 45]

print("\nOriginal numbers:", numbers)

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))

numbers.sort()

print("Sorted:", numbers)

numbers.reverse()

print("Reversed:", numbers)


# ============================================================
# 14. LIST COMPREHENSION
# ============================================================

print("\n--- List Comprehension ---")

squares = [x * x for x in range(1, 11)]

print("Squares:", squares)

even_numbers = [
    x for x in range(1, 51)
    if x % 2 == 0
]

print("Even numbers:", even_numbers)


# ============================================================
# 15. TUPLE
# ============================================================

print("\n--- Tuple ---")

coordinates = (10, 20, 30)

print("Coordinates:", coordinates)
print("First:", coordinates[0])
print("Length:", len(coordinates))


# ============================================================
# 16. SET
# ============================================================

print("\n--- Set ---")

values = {
    10,
    20,
    30,
    20,
    10,
    40
}

print("Set:", values)

values.add(50)
values.remove(30)

print("Updated set:", values)


# ============================================================
# 17. DICTIONARY
# ============================================================

print("\n--- Dictionary ---")

student = {
    "name": "Aman",
    "age": 21,
    "course": "Python",
    "marks": 88
}

print("Student:", student)

print("Name:", student["name"])
print("Age:", student["age"])
print("Marks:", student["marks"])

student["city"] = "Lucknow"
student["marks"] = 92

print("Updated student:", student)

print("\nDictionary items:")

for key, value in student.items():
    print(key, ":", value)


# ============================================================
# 18. FUNCTIONS
# ============================================================

print("\n--- Functions ---")


def greet(name):
    print("Hello", name)


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


greet("Rahul")

result1 = add(10, 20)
result2 = multiply(5, 6)

print("Addition:", result1)
print("Multiplication:", result2)


# ============================================================
# 19. FUNCTION WITH DEFAULT ARGUMENT
# ============================================================

def introduce(name, age=18):
    print("Name:", name)
    print("Age:", age)


introduce("Aman")
introduce("Rohit", 25)


# ============================================================
# 20. PRIME NUMBER FUNCTION
# ============================================================

def is_prime(number):

    if number <= 1:
        return False

    for i in range(2, int(math.sqrt(number)) + 1):

        if number % i == 0:
            return False

    return True


print("\n--- Prime Numbers ---")

for number in range(1, 51):

    if is_prime(number):
        print(number, end=" ")

print()


# ============================================================
# 21. RECURSION
# ============================================================

def recursive_factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * recursive_factorial(n - 1)


print("\nRecursive factorial of 5:")
print(recursive_factorial(5))


# ============================================================
# 22. FIBONACCI
# ============================================================

print("\n--- Fibonacci Series ---")

a = 0
b = 1

for i in range(10):

    print(a, end=" ")

    a, b = b, a + b

print()


# ============================================================
# 23. NESTED LOOPS
# ============================================================

print("\n--- Pattern ---")

for i in range(1, 6):

    for j in range(i):
        print("*", end=" ")

    print()


# ============================================================
# 24. NUMBER PATTERN
# ============================================================

print("\n--- Number Pattern ---")

for i in range(1, 6):

    for j in range(1, i + 1):
        print(j, end=" ")

    print()


# ============================================================
# 25. STRING REVERSING
# ============================================================

print("\n--- Reverse String ---")

text = input("Enter a word: ")

reverse_text = text[::-1]

print("Original:", text)
print("Reverse:", reverse_text)


# ============================================================
# 26. PALINDROME
# ============================================================

print("\n--- Palindrome ---")

word = input("Enter a word: ")

if word.lower() == word.lower()[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


# ============================================================
# 27. COUNT VOWELS
# ============================================================

print("\n--- Vowel Counter ---")

sentence = input("Enter a sentence: ")

vowels = "aeiou"

vowel_count = 0

for character in sentence.lower():

    if character in vowels:
        vowel_count += 1

print("Total vowels:", vowel_count)


# ============================================================
# 28. CHARACTER FREQUENCY
# ============================================================

print("\n--- Character Frequency ---")

text = input("Enter text: ")

frequency = {}

for character in text:

    if character in frequency:
        frequency[character] += 1
    else:
        frequency[character] = 1

for character, count in frequency.items():
    print(repr(character), ":", count)


# ============================================================
# 29. EXCEPTION HANDLING
# ============================================================

print("\n--- Exception Handling ---")

try:

    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))

    result = x / y

    print("Result:", result)

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

except Exception as error:
    print("Something went wrong:", error)

finally:
    print("Program finished this operation.")


# ============================================================
# 30. RANDOM NUMBER GAME
# ============================================================

print("\n--- Guessing Game ---")

secret_number = random.randint(1, 20)

attempts = 0

while True:

    try:
        guess = int(input("Guess a number between 1 and 20: "))
        attempts += 1

        if guess < secret_number:
            print("Too low!")

        elif guess > secret_number:
            print("Too high!")

        else:
            print("Correct!")
            print("Attempts:", attempts)
            break

    except ValueError:
        print("Enter a valid number.")


# ============================================================
# 31. CLASS AND OBJECT
# ============================================================

print("\n--- Class Practice ---")


class Student:

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)

    def passed(self):

        if self.marks >= 40:
            return True

        return False


student1 = Student("Rahul", 20, 85)
student2 = Student("Aman", 21, 35)

student1.display()

if student1.passed():
    print("Student 1 passed.")

student2.display()

if student2.passed():
    print("Student 2 passed.")
else:
    print("Student 2 failed.")


# ============================================================
# 32. INHERITANCE
# ============================================================

print("\n--- Inheritance ---")


class Animal:

    def speak(self):
        print("Animal makes a sound.")


class Dog(Animal):

    def speak(self):
        print("Dog says: Woof!")


class Cat(Animal):

    def speak(self):
        print("Cat says: Meow!")


animal = Animal()
dog = Dog()
cat = Cat()

animal.speak()
dog.speak()
cat.speak()


# ============================================================
# 33. FILE HANDLING
# ============================================================

print("\n--- File Handling ---")

filename = "practice.txt"

try:

    with open(filename, "w") as file:

        file.write("Python practice file\n")
        file.write("This is a test.\n")
        file.write("Learning Python is fun.\n")

    print("File created successfully.")

    with open(filename, "r") as file:

        content = file.read()

    print("\nFile content:")
    print(content)

except Exception as error:

    print("File error:", error)


# ============================================================
# 34. SEARCH IN LIST
# ============================================================

print("\n--- Search ---")

names = [
    "Rahul",
    "Aman",
    "Rohit",
    "Priya",
    "Neha",
    "Anjali"
]

search_name = input("Enter name to search: ")

if search_name in names:
    print("Name found.")
else:
    print("Name not found.")


# ============================================================
# 35. MINI MENU
# ============================================================

print("\n--- Mini Menu ---")

while True:

    print("\n1. Say Hello")
    print("2. Show Numbers")
    print("3. Show Squares")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        print("Hello! Welcome to Python practice.")

    elif choice == "2":

        for i in range(1, 11):
            print(i)

    elif choice == "3":

        for i in range(1, 11):
            print(i, "=", i * i)

    elif choice == "4":

        print("Goodbye!")
        break

    else:

        print("Invalid choice.")


# ============================================================
# 36. FINAL MESSAGE
# ============================================================

print("\n" + "=" * 60)
print("       PYTHON PRACTICE PROGRAM COMPLETED")
print("=" * 60)

print("Keep practicing!")
print("Try changing the code and experiment with it.")
