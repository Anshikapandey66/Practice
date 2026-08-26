# ============================================================
#             PYTHON PRACTICE PROGRAM - 2
# ============================================================

import random
import string
from datetime import datetime


# ============================================================
# 1. WELCOME
# ============================================================

print("=" * 60)
print("           PYTHON PRACTICE PROGRAM")
print("=" * 60)

name = input("Enter your name: ")

print(f"\nWelcome, {name}!")
print("Let's start practicing Python.\n")


# ============================================================
# 2. BASIC OPERATIONS
# ============================================================

def basic_operations():

    print("\n--- BASIC OPERATIONS ---")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nResults:")

    print("Addition       :", num1 + num2)
    print("Subtraction    :", num1 - num2)
    print("Multiplication :", num1 * num2)

    if num2 != 0:
        print("Division       :", num1 / num2)
        print("Floor Division :", num1 // num2)
        print("Remainder      :", num1 % num2)
    else:
        print("Division       : Cannot divide by zero")

    print("Power          :", num1 ** num2)


# ============================================================
# 3. EVEN / ODD
# ============================================================

def even_odd():

    print("\n--- EVEN / ODD CHECKER ---")

    number = int(input("Enter a number: "))

    if number % 2 == 0:
        print(number, "is EVEN")
    else:
        print(number, "is ODD")


# ============================================================
# 4. POSITIVE / NEGATIVE / ZERO
# ============================================================

def number_type():

    print("\n--- NUMBER TYPE ---")

    number = float(input("Enter a number: "))

    if number > 0:
        print("Positive number")

    elif number < 0:
        print("Negative number")

    else:
        print("Zero")


# ============================================================
# 5. MULTIPLICATION TABLE
# ============================================================

def multiplication_table():

    print("\n--- MULTIPLICATION TABLE ---")

    number = int(input("Enter number: "))

    for i in range(1, 21):

        result = number * i

        print(f"{number} x {i} = {result}")


# ============================================================
# 6. FACTORIAL
# ============================================================

def factorial():

    print("\n--- FACTORIAL ---")

    number = int(input("Enter number: "))

    if number < 0:

        print("Negative number ka factorial nahi hota.")
        return

    result = 1

    for i in range(1, number + 1):

        result = result * i

    print("Factorial:", result)


# ============================================================
# 7. PRIME NUMBER
# ============================================================

def check_prime():

    print("\n--- PRIME NUMBER CHECK ---")

    number = int(input("Enter number: "))

    if number <= 1:

        print("Not a prime number")
        return

    prime = True

    for i in range(2, number):

        if number % i == 0:

            prime = False
            break

    if prime:
        print(number, "is PRIME")
    else:
        print(number, "is NOT PRIME")


# ============================================================
# 8. PRIME NUMBERS IN RANGE
# ============================================================

def prime_range():

    print("\n--- PRIME NUMBERS IN RANGE ---")

    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))

    print("\nPrime numbers:")

    for number in range(start, end + 1):

        if number < 2:
            continue

        is_prime = True

        for i in range(2, number):

            if number % i == 0:

                is_prime = False
                break

        if is_prime:
            print(number, end=" ")

    print()


# ============================================================
# 9. FIBONACCI
# ============================================================

def fibonacci():

    print("\n--- FIBONACCI SERIES ---")

    count = int(input("How many terms? "))

    first = 0
    second = 1

    for i in range(count):

        print(first, end=" ")

        first, second = second, first + second

    print()


# ============================================================
# 10. REVERSE NUMBER
# ============================================================

def reverse_number():

    print("\n--- REVERSE NUMBER ---")

    number = input("Enter number: ")

    reversed_number = number[::-1]

    print("Original :", number)
    print("Reversed :", reversed_number)


# ============================================================
# 11. PALINDROME
# ============================================================

def palindrome():

    print("\n--- PALINDROME CHECK ---")

    text = input("Enter text: ")

    cleaned = text.lower().replace(" ", "")

    if cleaned == cleaned[::-1]:

        print("Palindrome hai.")

    else:

        print("Palindrome nahi hai.")


# ============================================================
# 12. VOWEL / CONSONANT
# ============================================================

def vowel_counter():

    print("\n--- VOWEL COUNTER ---")

    text = input("Enter a sentence: ")

    vowels = "aeiou"

    count = 0

    for character in text.lower():

        if character in vowels:

            count += 1

    print("Total vowels:", count)


# ============================================================
# 13. WORD COUNTER
# ============================================================

def word_counter():

    print("\n--- WORD COUNTER ---")

    sentence = input("Enter a sentence: ")

    words = sentence.split()

    print("Total words:", len(words))

    print("\nWords:")

    for word in words:

        print(word)


# ============================================================
# 14. LIST PRACTICE
# ============================================================

def list_practice():

    print("\n--- LIST PRACTICE ---")

    numbers = []

    count = int(input("How many numbers? "))

    for i in range(count):

        number = int(input(f"Enter number {i + 1}: "))

        numbers.append(number)

    print("\nList:", numbers)

    if numbers:

        print("Maximum:", max(numbers))
        print("Minimum:", min(numbers))
        print("Sum:", sum(numbers))
        print("Average:", sum(numbers) / len(numbers))

    print("\nSorted list:")

    numbers.sort()

    print(numbers)


# ============================================================
# 15. REMOVE DUPLICATES
# ============================================================

def remove_duplicates():

    print("\n--- REMOVE DUPLICATES ---")

    numbers = [10, 20, 10, 30, 40, 20, 50, 30, 60]

    print("Original list:")
    print(numbers)

    unique = []

    for number in numbers:

        if number not in unique:

            unique.append(number)

    print("\nWithout duplicates:")
    print(unique)


# ============================================================
# 16. DICTIONARY STUDENT
# ============================================================

def student_dictionary():

    print("\n--- STUDENT DICTIONARY ---")

    student = {}

    student["name"] = input("Enter name: ")
    student["age"] = int(input("Enter age: "))
    student["course"] = input("Enter course: ")
    student["marks"] = float(input("Enter marks: "))

    print("\nStudent Details:")

    for key, value in student.items():

        print(key.capitalize(), ":", value)

    if student["marks"] >= 40:

        print("\nStatus: PASS")

    else:

        print("\nStatus: FAIL")


# ============================================================
# 17. SHOPPING CART
# ============================================================

def shopping_cart():

    print("\n--- SHOPPING CART ---")

    products = {
        "Laptop": 55000,
        "Phone": 25000,
        "Keyboard": 1500,
        "Mouse": 800,
        "Headphones": 2000,
        "Monitor": 12000
    }

    cart = []

    while True:

        print("\nAvailable Products:")

        for product, price in products.items():

            print(f"{product} - ₹{price}")

        item = input(
            "\nEnter product name "
            "(or 'done' to finish): "
        )

        if item.lower() == "done":
            break

        if item in products:

            cart.append(item)

            print(item, "added to cart.")

        else:

            print("Product not found.")

    print("\n--- BILL ---")

    total = 0

    for item in cart:

        price = products[item]

        print(f"{item:<15} ₹{price}")

        total += price

    print("-" * 30)
    print(f"Total: ₹{total}")


# ============================================================
# 18. PASSWORD GENERATOR
# ============================================================

def password_generator():

    print("\n--- PASSWORD GENERATOR ---")

    length = int(input("Enter password length: "))

    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    password = ""

    for i in range(length):

        password += random.choice(characters)

    print("\nGenerated Password:")
    print(password)


# ============================================================
# 19. NUMBER GUESSING GAME
# ============================================================

def guessing_game():

    print("\n--- NUMBER GUESSING GAME ---")

    secret = random.randint(1, 100)

    attempts = 0

    while True:

        try:

            guess = int(input("Guess number 1-100: "))

            attempts += 1

            if guess < secret:

                print("Too LOW!")

            elif guess > secret:

                print("Too HIGH!")

            else:

                print("\nCorrect!")
                print("Attempts:", attempts)

                break

        except ValueError:

            print("Please enter a valid number.")


# ============================================================
# 20. ROCK PAPER SCISSORS
# ============================================================

def rock_paper_scissors():

    print("\n--- ROCK PAPER SCISSORS ---")

    choices = [
        "rock",
        "paper",
        "scissors"
    ]

    user_score = 0
    computer_score = 0

    for round_number in range(1, 6):

        print("\nRound", round_number)

        user = input(
            "Choose rock/paper/scissors: "
        ).lower()

        if user not in choices:

            print("Invalid choice.")
            continue

        computer = random.choice(choices)

        print("Computer:", computer)

        if user == computer:

            print("Draw!")

        elif (
            user == "rock"
            and computer == "scissors"
        ) or (
            user == "paper"
            and computer == "rock"
        ) or (
            user == "scissors"
            and computer == "paper"
        ):

            print("You win!")

            user_score += 1

        else:

            print("Computer wins!")

            computer_score += 1

    print("\nFinal Score")

    print("You     :", user_score)
    print("Computer:", computer_score)


# ============================================================
# 21. SIMPLE BANK ACCOUNT CLASS
# ============================================================

class BankAccount:

    def __init__(self, name, balance=0):

        self.name = name
        self.balance = balance

    def deposit(self, amount):

        if amount > 0:

            self.balance += amount

            print("Deposit successful.")

        else:

            print("Invalid amount.")

    def withdraw(self, amount):

        if amount <= 0:

            print("Invalid amount.")

        elif amount > self.balance:

            print("Insufficient balance.")

        else:

            self.balance -= amount

            print("Withdrawal successful.")

    def show_balance(self):

        print("\nAccount Holder:", self.name)
        print("Balance:", self.balance)


# ============================================================
# 22. BANK PROGRAM
# ============================================================

def bank_program():

    print("\n--- BANK PROGRAM ---")

    account_name = input("Enter account holder name: ")

    account = BankAccount(account_name)

    while True:

        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Balance")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":

            amount = float(input("Deposit amount: "))

            account.deposit(amount)

        elif choice == "2":

            amount = float(input("Withdraw amount: "))

            account.withdraw(amount)

        elif choice == "3":

            account.show_balance()

        elif choice == "4":

            print("Bank program closed.")

            break

        else:

            print("Invalid choice.")


# ============================================================
# 23. FILE HANDLING
# ============================================================

def file_practice():

    print("\n--- FILE HANDLING ---")

    filename = "python_notes.txt"

    try:

        with open(filename, "w") as file:

            file.write("Python Practice\n")
            file.write("Variables\n")
            file.write("Loops\n")
            file.write("Functions\n")
            file.write("Classes\n")

        print("File successfully created.")

        with open(filename, "r") as file:

            data = file.read()

        print("\nFile Data:")
        print(data)

    except Exception as error:

        print("Error:", error)


# ============================================================
# 24. DATE AND TIME
# ============================================================

def date_time():

    print("\n--- DATE AND TIME ---")

    now = datetime.now()

    print("Current Date and Time:")
    print(now)

    print("\nDate:")
    print(now.date())

    print("\nTime:")
    print(now.time())

    print("\nYear:", now.year)
    print("Month:", now.month)
    print("Day:", now.day)


# ============================================================
# 25. MAIN MENU
# ============================================================

def main_menu():

    while True:

        print("\n")
        print("=" * 60)
        print("                 MAIN MENU")
        print("=" * 60)

        print("1.  Basic Operations")
        print("2.  Even / Odd")
        print("3.  Positive / Negative")
        print("4.  Multiplication Table")
        print("5.  Factorial")
        print("6.  Prime Check")
        print("7.  Prime Numbers in Range")
        print("8.  Fibonacci")
        print("9.  Reverse Number")
        print("10. Palindrome")
        print("11. Vowel Counter")
        print("12. Word Counter")
        print("13. List Practice")
        print("14. Remove Duplicates")
        print("15. Student Dictionary")
        print("16. Shopping Cart")
        print("17. Password Generator")
        print("18. Number Guessing Game")
        print("19. Rock Paper Scissors")
        print("20. Bank Account")
        print("21. File Handling")
        print("22. Date and Time")
        print("23. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            basic_operations()

        elif choice == "2":
            even_odd()

        elif choice == "3":
            number_type()

        elif choice == "4":
            multiplication_table()

        elif choice == "5":
            factorial()

        elif choice == "6":
            check_prime()

        elif choice == "7":
            prime_range()

        elif choice == "8":
            fibonacci()

        elif choice == "9":
            reverse_number()

        elif choice == "10":
            palindrome()

        elif choice == "11":
            vowel_counter()

        elif choice == "12":
            word_counter()

        elif choice == "13":
            list_practice()

        elif choice == "14":
            remove_duplicates()

        elif choice == "15":
            student_dictionary()

        elif choice == "16":
            shopping_cart()

        elif choice == "17":
            password_generator()

        elif choice == "18":
            guessing_game()

        elif choice == "19":
            rock_paper_scissors()

        elif choice == "20":
            bank_program()

        elif choice == "21":
            file_practice()

        elif choice == "22":
            date_time()

        elif choice == "23":

            print("\nThanks for practicing Python!")
            print("Goodbye!")

            break

        else:

            print("\nInvalid choice. Try again.")


# ============================================================
# 26. START PROGRAM
# ============================================================

main_menu()
