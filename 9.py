# ============================================================
#                  PYTHON PRACTICE CODE - 5
# ============================================================

import random
import math
import time


# ============================================================
# 1. BASIC HELPERS
# ============================================================

def title(text):
    print("\n" + "=" * 70)
    print(text.center(70))
    print("=" * 70)


def pause():
    input("\nPress ENTER to continue...")


# ============================================================
# 2. TEMPERATURE CONVERTER
# ============================================================

def temperature_converter():

    title("TEMPERATURE CONVERTER")

    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    choice = input("Choose: ")

    try:

        value = float(input("Enter temperature: "))

        if choice == "1":

            result = (value * 9 / 5) + 32
            print("Fahrenheit:", result)

        elif choice == "2":

            result = (value - 32) * 5 / 9
            print("Celsius:", result)

        elif choice == "3":

            result = value + 273.15
            print("Kelvin:", result)

        elif choice == "4":

            result = value - 273.15
            print("Celsius:", result)

        else:

            print("Invalid choice.")

    except ValueError:

        print("Enter a valid number.")


# ============================================================
# 3. SIMPLE INTEREST
# ============================================================

def simple_interest():

    title("SIMPLE INTEREST")

    try:

        principal = float(
            input("Principal amount: ")
        )

        rate = float(
            input("Rate of interest: ")
        )

        time_years = float(
            input("Time in years: ")
        )

        interest = (
            principal
            * rate
            * time_years
            / 100
        )

        total = principal + interest

        print("\nInterest:", interest)
        print("Total Amount:", total)

    except ValueError:

        print("Invalid input.")


# ============================================================
# 4. COMPOUND INTEREST
# ============================================================

def compound_interest():

    title("COMPOUND INTEREST")

    try:

        principal = float(
            input("Principal: ")
        )

        rate = float(
            input("Rate: ")
        )

        years = int(
            input("Years: ")
        )

        amount = (
            principal
            * (1 + rate / 100) ** years
        )

        interest = amount - principal

        print("\nFinal Amount:", amount)
        print("Interest:", interest)

    except ValueError:

        print("Invalid input.")


# ============================================================
# 5. PRIME FACTORS
# ============================================================

def prime_factors():

    title("PRIME FACTORS")

    number = int(
        input("Enter number: ")
    )

    factors = []

    divisor = 2

    while number > 1:

        while number % divisor == 0:

            factors.append(divisor)

            number //= divisor

        divisor += 1

    print("Prime factors:", factors)


# ============================================================
# 6. BINARY CONVERTER
# ============================================================

def binary_converter():

    title("BINARY CONVERTER")

    number = int(
        input("Enter decimal number: ")
    )

    if number == 0:

        print("Binary: 0")
        return

    original = number

    binary = ""

    while number > 0:

        remainder = number % 2

        binary = str(remainder) + binary

        number //= 2

    print(
        f"{original} in binary = {binary}"
    )


# ============================================================
# 7. BINARY TO DECIMAL
# ============================================================

def binary_to_decimal():

    title("BINARY TO DECIMAL")

    binary = input(
        "Enter binary number: "
    )

    decimal = 0
    power = 0

    for digit in binary[::-1]:

        if digit not in "01":

            print("Invalid binary number.")
            return

        decimal += (
            int(digit)
            * (2 ** power)
        )

        power += 1

    print("Decimal:", decimal)


# ============================================================
# 8. BUBBLE SORT
# ============================================================

def bubble_sort():

    title("BUBBLE SORT")

    numbers = [
        64, 34, 25, 12,
        22, 11, 90, 5
    ]

    print("Original:", numbers)

    n = len(numbers)

    for i in range(n):

        swapped = False

        for j in range(0, n - i - 1):

            if numbers[j] > numbers[j + 1]:

                numbers[j], numbers[j + 1] = (
                    numbers[j + 1],
                    numbers[j]
                )

                swapped = True

        if not swapped:

            break

    print("Sorted:", numbers)


# ============================================================
# 9. SELECTION SORT
# ============================================================

def selection_sort():

    title("SELECTION SORT")

    numbers = [
        29, 10, 14,
        37, 13, 5,
        42, 8
    ]

    print("Original:", numbers)

    for i in range(len(numbers)):

        minimum_index = i

        for j in range(i + 1, len(numbers)):

            if (
                numbers[j]
                < numbers[minimum_index]
            ):

                minimum_index = j

        numbers[i], numbers[minimum_index] = (
            numbers[minimum_index],
            numbers[i]
        )

    print("Sorted:", numbers)


# ============================================================
# 10. BINARY SEARCH
# ============================================================

def binary_search():

    title("BINARY SEARCH")

    numbers = [
        5, 10, 15, 20,
        25, 30, 35, 40,
        45, 50
    ]

    target = int(
        input("Enter number: ")
    )

    left = 0
    right = len(numbers) - 1

    found = False

    while left <= right:

        middle = (left + right) // 2

        if numbers[middle] == target:

            print(
                "Found at index:",
                middle
            )

            found = True
            break

        elif numbers[middle] < target:

            left = middle + 1

        else:

            right = middle - 1

    if not found:

        print("Number not found.")


# ============================================================
# 11. RECURSIVE SUM
# ============================================================

def recursive_sum(n):

    if n <= 0:

        return 0

    return n + recursive_sum(n - 1)


def recursive_sum_program():

    title("RECURSIVE SUM")

    n = int(
        input("Enter number: ")
    )

    print(
        "Sum:",
        recursive_sum(n)
    )


# ============================================================
# 12. RECURSIVE FIBONACCI
# ============================================================

def recursive_fibonacci(n):

    if n <= 1:

        return n

    return (
        recursive_fibonacci(n - 1)
        + recursive_fibonacci(n - 2)
    )


def fibonacci_program():

    title("RECURSIVE FIBONACCI")

    count = int(
        input("How many terms: ")
    )

    for i in range(count):

        print(
            recursive_fibonacci(i),
            end=" "
        )

    print()


# ============================================================
# 13. ANAGRAM CHECKER
# ============================================================

def anagram_checker():

    title("ANAGRAM CHECKER")

    first = input(
        "Enter first word: "
    ).lower().replace(" ", "")

    second = input(
        "Enter second word: "
    ).lower().replace(" ", "")

    if sorted(first) == sorted(second):

        print("They are anagrams.")

    else:

        print("They are not anagrams.")


# ============================================================
# 14. CHARACTER ANALYZER
# ============================================================

def character_analyzer():

    title("CHARACTER ANALYZER")

    text = input("Enter text: ")

    letters = 0
    digits = 0
    spaces = 0
    special = 0

    for char in text:

        if char.isalpha():

            letters += 1

        elif char.isdigit():

            digits += 1

        elif char.isspace():

            spaces += 1

        else:

            special += 1

    print("\nLetters :", letters)
    print("Digits  :", digits)
    print("Spaces  :", spaces)
    print("Special :", special)


# ============================================================
# 15. SHOPPING CART CLASS
# ============================================================

class ShoppingCart:

    def __init__(self):

        self.items = []

    def add_item(self, name, price, quantity):

        item = {
            "name": name,
            "price": price,
            "quantity": quantity
        }

        self.items.append(item)

        print("Item added.")

    def remove_item(self, name):

        for item in self.items:

            if item["name"].lower() == name.lower():

                self.items.remove(item)

                print("Item removed.")
                return

        print("Item not found.")

    def total(self):

        total = 0

        for item in self.items:

            total += (
                item["price"]
                * item["quantity"]
            )

        return total

    def display(self):

        if not self.items:

            print("Cart is empty.")
            return

        print("\nCart:")

        for item in self.items:

            amount = (
                item["price"]
                * item["quantity"]
            )

            print(
                item["name"],
                "|",
                item["quantity"],
                "x",
                item["price"],
                "=",
                amount
            )

        print(
            "\nTotal:",
            self.total()
        )


# ============================================================
# 16. SHOPPING PROGRAM
# ============================================================

def shopping_program():

    title("SHOPPING CART")

    cart = ShoppingCart()

    while True:

        print("\n1. Add Item")
        print("2. Remove Item")
        print("3. Show Cart")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":

            name = input("Item name: ")

            try:

                price = float(
                    input("Price: ")
                )

                quantity = int(
                    input("Quantity: ")
                )

                cart.add_item(
                    name,
                    price,
                    quantity
                )

            except ValueError:

                print("Invalid input.")

        elif choice == "2":

            name = input(
                "Item to remove: "
            )

            cart.remove_item(name)

        elif choice == "3":

            cart.display()

        elif choice == "4":

            break

        else:

            print("Invalid choice.")


# ============================================================
# 17. INHERITANCE
# ============================================================

class Person:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def display(self):

        print(
            "Name:",
            self.name
        )

        print(
            "Age:",
            self.age
        )


class Student(Person):

    def __init__(
        self,
        name,
        age,
        course,
        marks
    ):

        super().__init__(
            name,
            age
        )

        self.course = course
        self.marks = marks

    def display(self):

        super().display()

        print(
            "Course:",
            self.course
        )

        print(
            "Marks:",
            self.marks
        )


def inheritance_program():

    title("INHERITANCE")

    student = Student(
        "Rahul",
        21,
        "Python",
        89
    )

    student.display()


# ============================================================
# 18. POLYMORPHISM
# ============================================================

class Dog:

    def sound(self):

        print("Dog: Woof!")


class Cat:

    def sound(self):

        print("Cat: Meow!")


class Cow:

    def sound(self):

        print("Cow: Moo!")


def polymorphism_program():

    title("POLYMORPHISM")

    animals = [
        Dog(),
        Cat(),
        Cow()
    ]

    for animal in animals:

        animal.sound()


# ============================================================
# 19. BANK ACCOUNT
# ============================================================

class BankAccount:

    def __init__(
        self,
        owner,
        balance=0
    ):

        self.owner = owner
        self.balance = balance

    def deposit(self, amount):

        if amount <= 0:

            print("Invalid amount.")
            return

        self.balance += amount

        print("Deposit successful.")

    def withdraw(self, amount):

        if amount <= 0:

            print("Invalid amount.")
            return

        if amount > self.balance:

            print("Insufficient balance.")
            return

        self.balance -= amount

        print("Withdrawal successful.")

    def show_balance(self):

        print(
            "\nOwner:",
            self.owner
        )

        print(
            "Balance:",
            self.balance
        )


def bank_program():

    title("BANK")

    name = input(
        "Account holder: "
    )

    account = BankAccount(name)

    while True:

        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Balance")
        print("4. Exit")

        choice = input("Choice: ")

        try:

            if choice == "1":

                amount = float(
                    input("Amount: ")
                )

                account.deposit(amount)

            elif choice == "2":

                amount = float(
                    input("Amount: ")
                )

                account.withdraw(amount)

            elif choice == "3":

                account.show_balance()

            elif choice == "4":

                break

            else:

                print("Invalid choice.")

        except ValueError:

            print("Enter a valid amount.")


# ============================================================
# 20. DICE ROLL SIMULATOR
# ============================================================

def dice_simulator():

    title("DICE SIMULATOR")

    rolls = int(
        input("How many rolls: ")
    )

    results = []

    for i in range(rolls):

        value = random.randint(1, 6)

        results.append(value)

    print("\nResults:")
    print(results)

    print("\nStatistics:")

    for number in range(1, 7):

        count = results.count(number)

        print(
            number,
            "appeared",
            count,
            "times"
        )


# ============================================================
# 21. LOTTERY NUMBER GENERATOR
# ============================================================

def lottery():

    title("LOTTERY GENERATOR")

    numbers = []

    while len(numbers) < 6:

        number = random.randint(
            1,
            49
        )

        if number not in numbers:

            numbers.append(number)

    numbers.sort()

    print(
        "Your lottery numbers:"
    )

    print(numbers)


# ============================================================
# 22. QUIZ
# ============================================================

def quiz():

    title("GENERAL QUIZ")

    questions = [

        {
            "q": "Capital of India?",
            "a": "delhi"
        },

        {
            "q": "5 x 5 = ?",
            "a": "25"
        },

        {
            "q": "Python list uses which brackets?",
            "a": "[]"
        },

        {
            "q": "Which keyword creates a class?",
            "a": "class"
        },

        {
            "q": "What is 10 % 3?",
            "a": "1"
        }

    ]

    score = 0

    for question in questions:

        print(
            "\n",
            question["q"]
        )

        answer = input(
            "Answer: "
        ).lower().strip()

        if answer == question["a"]:

            print("Correct!")
            score += 1

        else:

            print(
                "Wrong.",
                "Correct:",
                question["a"]
            )

    print(
        "\nScore:",
        score,
        "/",
        len(questions)
    )


# ============================================================
# 23. MEMORY GAME
# ============================================================

def memory_game():

    title("MEMORY GAME")

    numbers = random.sample(
        range(1, 21),
        5
    )

    print(
        "Remember these numbers:"
    )

    print(numbers)

    time.sleep(3)

    print("\n" * 30)

    print(
        "Now enter the numbers "
        "you remember."
    )

    user_numbers = []

    for i in range(5):

        try:

            number = int(
                input(
                    f"Number {i + 1}: "
                )
            )

            user_numbers.append(
                number
            )

        except ValueError:

            print("Invalid number.")

    correct = 0

    for number in user_numbers:

        if number in numbers:

            correct += 1

    print(
        "\nYou remembered",
        correct,
        "correct numbers."
    )

    print(
        "Original numbers:",
        numbers
    )


# ============================================================
# 24. MAIN MENU
# ============================================================

def main():

    while True:

        title("PYTHON PRACTICE - 5")

        print("1.  Temperature Converter")
        print("2.  Simple Interest")
        print("3.  Compound Interest")
        print("4.  Prime Factors")
        print("5.  Decimal to Binary")
        print("6.  Binary to Decimal")
        print("7.  Bubble Sort")
        print("8.  Selection Sort")
        print("9.  Binary Search")
        print("10. Recursive Sum")
        print("11. Recursive Fibonacci")
        print("12. Anagram Checker")
        print("13. Character Analyzer")
        print("14. Shopping Cart")
        print("15. Inheritance")
        print("16. Polymorphism")
        print("17. Bank Account")
        print("18. Dice Simulator")
        print("19. Lottery Generator")
        print("20. Quiz")
        print("21. Memory Game")
        print("22. Exit")

        choice = input(
            "\nEnter choice: "
        )

        try:

            if choice == "1":
                temperature_converter()

            elif choice == "2":
                simple_interest()

            elif choice == "3":
                compound_interest()

            elif choice == "4":
                prime_factors()

            elif choice == "5":
                binary_converter()

            elif choice == "6":
                binary_to_decimal()

            elif choice == "7":
                bubble_sort()

            elif choice == "8":
                selection_sort()

            elif choice == "9":
                binary_search()

            elif choice == "10":
                recursive_sum_program()

            elif choice == "11":
                fibonacci_program()

            elif choice == "12":
                anagram_checker()

            elif choice == "13":
                character_analyzer()

            elif choice == "14":
                shopping_program()

            elif choice == "15":
                inheritance_program()

            elif choice == "16":
                polymorphism_program()

            elif choice == "17":
                bank_program()

            elif choice == "18":
                dice_simulator()

            elif choice == "19":
                lottery()

            elif choice == "20":
                quiz()

            elif choice == "21":
                memory_game()

            elif choice == "22":

                print(
                    "\nPython practice finished!"
                )

                break

            else:

                print(
                    "\nInvalid choice."
                )

        except ValueError:

            print(
                "\nPlease enter valid input."
            )


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":

    main()
