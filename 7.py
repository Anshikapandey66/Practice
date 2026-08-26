# ============================================================
#              PYTHON PRACTICE CODE - 3
# ============================================================

import random
import math


# ============================================================
# 1. BASIC UTILITY FUNCTIONS
# ============================================================

def line():
    print("-" * 60)


def title(text):
    print("\n")
    print("=" * 60)
    print(text.center(60))
    print("=" * 60)


# ============================================================
# 2. SIMPLE CALCULATOR
# ============================================================

def calculator():

    title("CALCULATOR")

    while True:

        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Modulus")
        print("7. Exit")

        choice = input("\nChoose operation: ")

        if choice == "7":
            break

        try:

            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", a + b)

            elif choice == "2":
                print("Result:", a - b)

            elif choice == "3":
                print("Result:", a * b)

            elif choice == "4":

                if b == 0:
                    print("Cannot divide by zero.")

                else:
                    print("Result:", a / b)

            elif choice == "5":
                print("Result:", a ** b)

            elif choice == "6":

                if b == 0:
                    print("Cannot use zero as divisor.")

                else:
                    print("Result:", a % b)

            else:
                print("Invalid choice.")

        except ValueError:

            print("Please enter valid numbers.")


# ============================================================
# 3. FACTORIAL
# ============================================================

def factorial(n):

    if n < 0:
        return None

    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


# ============================================================
# 4. RECURSIVE FACTORIAL
# ============================================================

def recursive_factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * recursive_factorial(n - 1)


# ============================================================
# 5. PRIME CHECK
# ============================================================

def is_prime(number):

    if number < 2:
        return False

    for i in range(2, int(math.sqrt(number)) + 1):

        if number % i == 0:
            return False

    return True


# ============================================================
# 6. PRIME PROGRAM
# ============================================================

def prime_program():

    title("PRIME NUMBER")

    number = int(input("Enter number: "))

    if is_prime(number):

        print(number, "is a prime number.")

    else:

        print(number, "is not a prime number.")

    print("\nPrime numbers from 1 to", number)

    for i in range(1, number + 1):

        if is_prime(i):
            print(i, end=" ")

    print()


# ============================================================
# 7. ARMSTRONG NUMBER
# ============================================================

def armstrong():

    title("ARMSTRONG NUMBER")

    number = int(input("Enter number: "))

    original = number

    digits = len(str(number))

    total = 0

    while number > 0:

        digit = number % 10

        total += digit ** digits

        number //= 10

    if total == original:

        print(original, "is an Armstrong number.")

    else:

        print(original, "is not an Armstrong number.")


# ============================================================
# 8. ARMSTRONG NUMBERS
# ============================================================

def armstrong_range():

    title("ARMSTRONG NUMBERS")

    start = int(input("Start: "))
    end = int(input("End: "))

    print("\nArmstrong numbers:")

    for number in range(start, end + 1):

        digits = len(str(number))
        temp = number
        total = 0

        while temp > 0:

            digit = temp % 10
            total += digit ** digits
            temp //= 10

        if total == number:

            print(number, end=" ")

    print()


# ============================================================
# 9. NUMBER STATISTICS
# ============================================================

def number_statistics():

    title("NUMBER STATISTICS")

    numbers = []

    n = int(input("How many numbers? "))

    for i in range(n):

        value = float(input(f"Number {i + 1}: "))

        numbers.append(value)

    print("\nNumbers:", numbers)

    if len(numbers) > 0:

        total = sum(numbers)
        average = total / len(numbers)

        print("Total:", total)
        print("Average:", average)
        print("Maximum:", max(numbers))
        print("Minimum:", min(numbers))

        even = 0
        odd = 0

        for number in numbers:

            if number % 2 == 0:
                even += 1
            else:
                odd += 1

        print("Even numbers:", even)
        print("Odd numbers:", odd)


# ============================================================
# 10. CUSTOM SORTING
# ============================================================

def custom_sort():

    title("CUSTOM SORTING")

    numbers = [
        45, 12, 89, 34, 2,
        67, 23, 91, 5, 56
    ]

    print("Original:", numbers)

    for i in range(len(numbers)):

        for j in range(0, len(numbers) - i - 1):

            if numbers[j] > numbers[j + 1]:

                numbers[j], numbers[j + 1] = (
                    numbers[j + 1],
                    numbers[j]
                )

    print("Sorted:", numbers)


# ============================================================
# 11. SEARCHING
# ============================================================

def linear_search():

    title("LINEAR SEARCH")

    numbers = [
        10, 25, 30, 45,
        50, 60, 75, 80
    ]

    target = int(input("Enter number to search: "))

    found = False

    for index in range(len(numbers)):

        if numbers[index] == target:

            print("Number found!")
            print("Index:", index)

            found = True
            break

    if not found:

        print("Number not found.")


# ============================================================
# 12. STUDENT MARKS
# ============================================================

def student_marks():

    title("STUDENT MARKS SYSTEM")

    students = {}

    total_students = int(
        input("Enter number of students: ")
    )

    for i in range(total_students):

        name = input(
            f"\nEnter student {i + 1} name: "
        )

        marks = float(
            input("Enter marks: ")
        )

        students[name] = marks

    print("\nStudent Results")

    line()

    for name, marks in students.items():

        if marks >= 90:
            grade = "A+"

        elif marks >= 80:
            grade = "A"

        elif marks >= 70:
            grade = "B"

        elif marks >= 60:
            grade = "C"

        elif marks >= 50:
            grade = "D"

        elif marks >= 40:
            grade = "E"

        else:
            grade = "F"

        print(
            f"{name:<20} "
            f"{marks:<10} "
            f"{grade}"
        )

    line()


# ============================================================
# 13. ATM CLASS
# ============================================================

class ATM:

    def __init__(self, balance=10000, pin="1234"):

        self.balance = balance
        self.pin = pin

    def check_pin(self):

        entered = input("Enter PIN: ")

        return entered == self.pin

    def show_balance(self):

        print("\nCurrent Balance:", self.balance)

    def deposit(self):

        try:

            amount = float(
                input("Enter deposit amount: ")
            )

            if amount <= 0:

                print("Invalid amount.")

            else:

                self.balance += amount

                print("Deposit successful.")

        except ValueError:

            print("Invalid input.")

    def withdraw(self):

        try:

            amount = float(
                input("Enter withdrawal amount: ")
            )

            if amount <= 0:

                print("Invalid amount.")

            elif amount > self.balance:

                print("Insufficient balance.")

            else:

                self.balance -= amount

                print("Please collect your cash.")

        except ValueError:

            print("Invalid input.")


# ============================================================
# 14. ATM PROGRAM
# ============================================================

def atm_program():

    title("ATM")

    atm = ATM()

    attempts = 3

    while attempts > 0:

        if atm.check_pin():

            print("\nLogin successful.")
            break

        attempts -= 1

        print(
            "Wrong PIN.",
            attempts,
            "attempt(s) remaining."
        )

    else:

        print("Card blocked.")
        return

    while True:

        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":

            atm.show_balance()

        elif choice == "2":

            atm.deposit()

        elif choice == "3":

            atm.withdraw()

        elif choice == "4":

            print("Thank you.")
            break

        else:

            print("Invalid choice.")


# ============================================================
# 15. PASSWORD STRENGTH
# ============================================================

def password_strength():

    title("PASSWORD CHECKER")

    password = input("Enter password: ")

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special = "!@#$%^&*()-_=+"

    for character in password:

        if character.isupper():
            has_upper = True

        elif character.islower():
            has_lower = True

        elif character.isdigit():
            has_digit = True

        elif character in special:
            has_special = True

    score = 0

    if len(password) >= 8:
        score += 1

    if has_upper:
        score += 1

    if has_lower:
        score += 1

    if has_digit:
        score += 1

    if has_special:
        score += 1

    print("\nPassword score:", score, "/ 5")

    if score == 5:

        print("Very Strong Password")

    elif score >= 4:

        print("Strong Password")

    elif score >= 3:

        print("Medium Password")

    else:

        print("Weak Password")


# ============================================================
# 16. RANDOM DICE
# ============================================================

def dice_game():

    title("DICE GAME")

    while True:

        input("Press ENTER to roll dice...")

        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("Dice 1:", dice1)
        print("Dice 2:", dice2)

        print("Total:", dice1 + dice2)

        again = input(
            "\nRoll again? (y/n): "
        ).lower()

        if again != "y":
            break


# ============================================================
# 17. QUIZ GAME
# ============================================================

def quiz_game():

    title("PYTHON QUIZ")

    questions = [

        {
            "question": "Which keyword defines a function?",
            "options": ["A. func", "B. def", "C. function", "D. define"],
            "answer": "B"
        },

        {
            "question": "Which data type stores True/False?",
            "options": ["A. int", "B. str", "C. bool", "D. list"],
            "answer": "C"
        },

        {
            "question": "Which symbol is used for comments?",
            "options": ["A. //", "B. #", "C. --", "D. /*"],
            "answer": "B"
        },

        {
            "question": "Which function gives list length?",
            "options": ["A. size()", "B. count()", "C. len()", "D. length()"],
            "answer": "C"
        },

        {
            "question": "Which keyword is used for a loop?",
            "options": ["A. repeat", "B. loop", "C. for", "D. foreach"],
            "answer": "C"
        }

    ]

    score = 0

    for number, question in enumerate(
        questions,
        start=1
    ):

        print(f"\nQuestion {number}")
        print(question["question"])

        for option in question["options"]:

            print(option)

        answer = input(
            "Your answer: "
        ).upper()

        if answer == question["answer"]:

            print("Correct!")
            score += 1

        else:

            print(
                "Wrong!",
                "Correct answer:",
                question["answer"]
            )

    print("\nFinal Score:", score, "/", len(questions))

    percentage = (
        score / len(questions)
    ) * 100

    print("Percentage:", percentage, "%")


# ============================================================
# 18. PASSWORD GENERATOR
# ============================================================

def password_generator():

    title("PASSWORD GENERATOR")

    letters = (
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    )

    digits = "0123456789"

    symbols = "!@#$%^&*"

    length = int(
        input("Password length: ")
    )

    password = ""

    for i in range(length):

        category = random.choice(
            [
                letters,
                digits,
                symbols
            ]
        )

        password += random.choice(category)

    print("\nGenerated password:")
    print(password)


# ============================================================
# 19. MATRIX
# ============================================================

def matrix_practice():

    title("MATRIX PRACTICE")

    matrix = [

        [1, 2, 3],

        [4, 5, 6],

        [7, 8, 9]

    ]

    print("Matrix:")

    for row in matrix:

        for value in row:

            print(value, end=" ")

        print()

    total = 0

    for row in matrix:

        for value in row:

            total += value

    print("\nTotal:", total)


# ============================================================
# 20. NESTED DICTIONARY
# ============================================================

def nested_dictionary():

    title("NESTED DICTIONARY")

    employees = {

        "E101": {
            "name": "Rahul",
            "age": 24,
            "salary": 35000
        },

        "E102": {
            "name": "Aman",
            "age": 27,
            "salary": 42000
        },

        "E103": {
            "name": "Priya",
            "age": 25,
            "salary": 39000
        }

    }

    for employee_id, data in employees.items():

        print("\nEmployee ID:", employee_id)

        for key, value in data.items():

            print(
                key.capitalize(),
                ":",
                value
            )


# ============================================================
# 21. MAIN MENU
# ============================================================

def main():

    while True:

        title("PYTHON PRACTICE MENU")

        print("1.  Calculator")
        print("2.  Prime Program")
        print("3.  Armstrong Check")
        print("4.  Armstrong Range")
        print("5.  Number Statistics")
        print("6.  Custom Sorting")
        print("7.  Linear Search")
        print("8.  Student Marks")
        print("9.  ATM")
        print("10. Password Strength")
        print("11. Dice Game")
        print("12. Python Quiz")
        print("13. Password Generator")
        print("14. Matrix Practice")
        print("15. Nested Dictionary")
        print("16. Factorial")
        print("17. Recursive Factorial")
        print("18. Exit")

        choice = input(
            "\nEnter your choice: "
        )

        if choice == "1":

            calculator()

        elif choice == "2":

            prime_program()

        elif choice == "3":

            armstrong()

        elif choice == "4":

            armstrong_range()

        elif choice == "5":

            number_statistics()

        elif choice == "6":

            custom_sort()

        elif choice == "7":

            linear_search()

        elif choice == "8":

            student_marks()

        elif choice == "9":

            atm_program()

        elif choice == "10":

            password_strength()

        elif choice == "11":

            dice_game()

        elif choice == "12":

            quiz_game()

        elif choice == "13":

            password_generator()

        elif choice == "14":

            matrix_practice()

        elif choice == "15":

            nested_dictionary()

        elif choice == "16":

            number = int(
                input("Enter number: ")
            )

            result = factorial(number)

            print("Factorial:", result)

        elif choice == "17":

            number = int(
                input("Enter number: ")
            )

            if number < 0:

                print("Invalid number.")

            else:

                print(
                    "Recursive factorial:",
                    recursive_factorial(number)
                )

        elif choice == "18":

            print("\nPython practice finished.")
            print("Keep coding! 🚀")
            break

        else:

            print("\nInvalid choice.")


# ============================================================
# 22. PROGRAM START
# ============================================================

if __name__ == "__main__":

    main()
