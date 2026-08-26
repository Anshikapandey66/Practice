# ============================================================
#                 PYTHON PRACTICE CODE - 4
# ============================================================

import random
import math


# ============================================================
# UTILITY
# ============================================================

def separator():
    print("-" * 65)


def heading(text):
    print("\n" + "=" * 65)
    print(text.center(65))
    print("=" * 65)


# ============================================================
# 1. NUMBER REVERSE
# ============================================================

def reverse_number():

    heading("REVERSE NUMBER")

    number = int(input("Enter number: "))

    original = number
    reverse = 0

    while number != 0:

        digit = number % 10

        reverse = reverse * 10 + digit

        number //= 10

    print("Original :", original)
    print("Reverse  :", reverse)


# ============================================================
# 2. DIGIT SUM
# ============================================================

def digit_sum():

    heading("DIGIT SUM")

    number = abs(int(input("Enter number: ")))

    total = 0

    while number > 0:

        digit = number % 10

        total += digit

        number //= 10

    print("Sum of digits:", total)


# ============================================================
# 3. DIGIT COUNT
# ============================================================

def digit_count():

    heading("DIGIT COUNT")

    number = abs(int(input("Enter number: ")))

    if number == 0:

        print("Digits: 1")
        return

    count = 0

    while number > 0:

        count += 1

        number //= 10

    print("Number of digits:", count)


# ============================================================
# 4. PERFECT NUMBER
# ============================================================

def perfect_number():

    heading("PERFECT NUMBER")

    number = int(input("Enter number: "))

    if number <= 0:

        print("Invalid number.")
        return

    total = 0

    for i in range(1, number):

        if number % i == 0:

            total += i

    if total == number:

        print(number, "is a perfect number.")

    else:

        print(number, "is not a perfect number.")


# ============================================================
# 5. PERFECT NUMBERS IN RANGE
# ============================================================

def perfect_range():

    heading("PERFECT NUMBERS IN RANGE")

    start = int(input("Start: "))
    end = int(input("End: "))

    print("\nPerfect numbers:")

    for number in range(start, end + 1):

        if number <= 0:
            continue

        total = 0

        for i in range(1, number):

            if number % i == 0:

                total += i

        if total == number:

            print(number, end=" ")

    print()


# ============================================================
# 6. GCD
# ============================================================

def gcd_program():

    heading("GCD")

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    while b != 0:

        a, b = b, a % b

    print("GCD:", abs(a))


# ============================================================
# 7. LCM
# ============================================================

def lcm_program():

    heading("LCM")

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if a == 0 or b == 0:

        print("LCM: 0")
        return

    x = abs(a)
    y = abs(b)

    while y != 0:

        x, y = y, x % y

    gcd = x

    lcm = abs(a * b) // gcd

    print("LCM:", lcm)


# ============================================================
# 8. FIBONACCI LIST
# ============================================================

def fibonacci_list():

    heading("FIBONACCI")

    count = int(input("Number of terms: "))

    sequence = []

    a = 0
    b = 1

    for i in range(count):

        sequence.append(a)

        a, b = b, a + b

    print("Fibonacci:")

    print(sequence)


# ============================================================
# 9. SECOND LARGEST
# ============================================================

def second_largest():

    heading("SECOND LARGEST")

    numbers = [
        12, 45, 23, 67,
        89, 34, 90, 56,
        90, 21
    ]

    unique = list(set(numbers))

    unique.sort()

    print("Numbers:", numbers)

    if len(unique) >= 2:

        print("Second largest:", unique[-2])

    else:

        print("Not enough unique numbers.")


# ============================================================
# 10. SECOND SMALLEST
# ============================================================

def second_smallest():

    heading("SECOND SMALLEST")

    numbers = [
        12, 5, 8, 3,
        15, 3, 9, 20
    ]

    unique = list(set(numbers))

    unique.sort()

    print("Numbers:", numbers)

    if len(unique) >= 2:

        print("Second smallest:", unique[1])

    else:

        print("Not enough unique numbers.")


# ============================================================
# 11. FREQUENCY OF NUMBERS
# ============================================================

def number_frequency():

    heading("NUMBER FREQUENCY")

    numbers = [
        1, 2, 3, 2, 4,
        5, 1, 2, 3, 5,
        2, 4, 4, 1
    ]

    frequency = {}

    for number in numbers:

        if number in frequency:

            frequency[number] += 1

        else:

            frequency[number] = 1

    print("Numbers:", numbers)

    print("\nFrequency:")

    for number, count in frequency.items():

        print(number, "=>", count)


# ============================================================
# 12. CHARACTER FREQUENCY
# ============================================================

def character_frequency():

    heading("CHARACTER FREQUENCY")

    text = input("Enter text: ")

    frequency = {}

    for char in text:

        if char == " ":

            continue

        if char in frequency:

            frequency[char] += 1

        else:

            frequency[char] = 1

    for char, count in frequency.items():

        print(char, "=>", count)


# ============================================================
# 13. WORD FREQUENCY
# ============================================================

def word_frequency():

    heading("WORD FREQUENCY")

    sentence = input("Enter sentence: ")

    words = sentence.lower().split()

    frequency = {}

    for word in words:

        if word in frequency:

            frequency[word] += 1

        else:

            frequency[word] = 1

    print()

    for word, count in frequency.items():

        print(word, "=>", count)


# ============================================================
# 14. REMOVE DUPLICATES WITHOUT SET
# ============================================================

def remove_duplicates():

    heading("REMOVE DUPLICATES")

    numbers = [
        10, 20, 10, 30,
        40, 20, 50, 30,
        60, 10
    ]

    result = []

    for number in numbers:

        if number not in result:

            result.append(number)

    print("Original:", numbers)
    print("Result  :", result)


# ============================================================
# 15. MERGE TWO LISTS
# ============================================================

def merge_lists():

    heading("MERGE TWO LISTS")

    list1 = [1, 3, 5, 7, 9]
    list2 = [2, 4, 6, 8, 10]

    result = []

    for item in list1:
        result.append(item)

    for item in list2:
        result.append(item)

    print("List 1:", list1)
    print("List 2:", list2)
    print("Merged:", result)


# ============================================================
# 16. LIST INTERSECTION
# ============================================================

def list_intersection():

    heading("LIST INTERSECTION")

    list1 = [1, 2, 3, 4, 5, 6]
    list2 = [4, 5, 6, 7, 8, 9]

    common = []

    for number in list1:

        if number in list2:

            common.append(number)

    print("List 1:", list1)
    print("List 2:", list2)
    print("Common:", common)


# ============================================================
# 17. MATRIX ADDITION
# ============================================================

def matrix_addition():

    heading("MATRIX ADDITION")

    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    matrix2 = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]

    result = []

    for i in range(3):

        row = []

        for j in range(3):

            value = (
                matrix1[i][j]
                + matrix2[i][j]
            )

            row.append(value)

        result.append(row)

    print("Result:")

    for row in result:

        print(row)


# ============================================================
# 18. MATRIX TRANSPOSE
# ============================================================

def matrix_transpose():

    heading("MATRIX TRANSPOSE")

    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    rows = len(matrix)
    columns = len(matrix[0])

    transpose = []

    for j in range(columns):

        row = []

        for i in range(rows):

            row.append(matrix[i][j])

        transpose.append(row)

    print("Original:")

    for row in matrix:
        print(row)

    print("\nTranspose:")

    for row in transpose:
        print(row)


# ============================================================
# 19. TIC TAC TOE
# ============================================================

def tic_tac_toe():

    heading("TIC TAC TOE")

    board = [
        " ", " ", " ",
        " ", " ", " ",
        " ", " ", " "
    ]

    current_player = "X"

    def show_board():

        print()

        print(
            f" {board[0]} | {board[1]} | {board[2]} "
        )

        print("---+---+---")

        print(
            f" {board[3]} | {board[4]} | {board[5]} "
        )

        print("---+---+---")

        print(
            f" {board[6]} | {board[7]} | {board[8]} "
        )

    def winner():

        combinations = [

            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),

            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),

            (0, 4, 8),
            (2, 4, 6)

        ]

        for a, b, c in combinations:

            if (
                board[a] != " "
                and board[a] == board[b]
                and board[b] == board[c]
            ):

                return board[a]

        return None

    for turn in range(9):

        show_board()

        print(
            "\nPlayer",
            current_player,
            "turn"
        )

        try:

            position = int(
                input(
                    "Choose position 1-9: "
                )
            ) - 1

            if position < 0 or position > 8:

                print("Invalid position.")
                continue

            if board[position] != " ":

                print("Position already taken.")
                continue

            board[position] = current_player

            result = winner()

            if result:

                show_board()

                print(
                    "\nPlayer",
                    result,
                    "wins!"
                )

                return

            if current_player == "X":

                current_player = "O"

            else:

                current_player = "X"

        except ValueError:

            print("Enter a number.")

    show_board()

    print("\nGame Draw!")


# ============================================================
# 20. NUMBER GUESSING
# ============================================================

def guessing_game():

    heading("NUMBER GUESSING")

    secret = random.randint(1, 100)

    attempts = 0

    while True:

        try:

            guess = int(
                input(
                    "Guess number 1-100: "
                )
            )

            attempts += 1

            if guess < secret:

                print("Too low!")

            elif guess > secret:

                print("Too high!")

            else:

                print(
                    "\nCorrect!",
                    "Attempts:",
                    attempts
                )

                break

        except ValueError:

            print("Please enter a number.")


# ============================================================
# 21. ROCK PAPER SCISSORS
# ============================================================

def rock_paper_scissors():

    heading("ROCK PAPER SCISSORS")

    choices = [
        "rock",
        "paper",
        "scissors"
    ]

    player_score = 0
    computer_score = 0

    for round_number in range(1, 6):

        print("\nRound", round_number)

        player = input(
            "rock/paper/scissors: "
        ).lower()

        if player not in choices:

            print("Invalid choice.")
            continue

        computer = random.choice(choices)

        print("Computer:", computer)

        if player == computer:

            print("Draw!")

        elif (
            player == "rock"
            and computer == "scissors"
        ) or (
            player == "paper"
            and computer == "rock"
        ) or (
            player == "scissors"
            and computer == "paper"
        ):

            print("You win!")

            player_score += 1

        else:

            print("Computer wins!")

            computer_score += 1

    print("\nFinal Score")
    print("Player  :", player_score)
    print("Computer:", computer_score)


# ============================================================
# 22. BANK ACCOUNT CLASS
# ============================================================

class BankAccount:

    def __init__(self, owner, balance=0):

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

    def display(self):

        print("\nAccount Holder:", self.owner)
        print("Balance:", self.balance)


# ============================================================
# 23. BANK PROGRAM
# ============================================================

def bank_program():

    heading("BANK ACCOUNT")

    owner = input("Account holder name: ")

    account = BankAccount(owner)

    while True:

        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Balance")
        print("4. Exit")

        choice = input("Choice: ")

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

            account.display()

        elif choice == "4":

            break

        else:

            print("Invalid choice.")


# ============================================================
# 24. EMPLOYEE DATA
# ============================================================

def employee_system():

    heading("EMPLOYEE SYSTEM")

    employees = []

    count = int(
        input("Number of employees: ")
    )

    for i in range(count):

        print("\nEmployee", i + 1)

        name = input("Name: ")

        age = int(
            input("Age: ")
        )

        salary = float(
            input("Salary: ")
        )

        employee = {
            "name": name,
            "age": age,
            "salary": salary
        }

        employees.append(employee)

    print("\nEmployee List")

    separator()

    for employee in employees:

        print(
            "Name:",
            employee["name"]
        )

        print(
            "Age:",
            employee["age"]
        )

        print(
            "Salary:",
            employee["salary"]
        )

        separator()


# ============================================================
# 25. PASSWORD VALIDATOR
# ============================================================

def password_validator():

    heading("PASSWORD VALIDATOR")

    password = input("Enter password: ")

    upper = False
    lower = False
    digit = False
    special = False

    symbols = "!@#$%^&*"

    for char in password:

        if char.isupper():

            upper = True

        if char.islower():

            lower = True

        if char.isdigit():

            digit = True

        if char in symbols:

            special = True

    print("\nPassword requirements:")

    print("Length >= 8 :", len(password) >= 8)
    print("Uppercase   :", upper)
    print("Lowercase   :", lower)
    print("Digit       :", digit)
    print("Special     :", special)

    if (
        len(password) >= 8
        and upper
        and lower
        and digit
        and special
    ):

        print("\nStrong password!")

    else:

        print("\nPassword is weak.")


# ============================================================
# 26. SHOPPING BILL
# ============================================================

def shopping_bill():

    heading("SHOPPING BILL")

    products = {}

    while True:

        name = input(
            "\nProduct name "
            "(type done to finish): "
        )

        if name.lower() == "done":

            break

        try:

            price = float(
                input("Price: ")
            )

            quantity = int(
                input("Quantity: ")
            )

            products[name] = {
                "price": price,
                "quantity": quantity
            }

        except ValueError:

            print("Invalid input.")

    print("\n" + "=" * 65)

    print(
        f"{'Product':<20}"
        f"{'Price':<12}"
        f"{'Qty':<8}"
        f"{'Total':<12}"
    )

    print("=" * 65)

    grand_total = 0

    for name, data in products.items():

        total = (
            data["price"]
            * data["quantity"]
        )

        grand_total += total

        print(
            f"{name:<20}"
            f"{data['price']:<12}"
            f"{data['quantity']:<8}"
            f"{total:<12}"
        )

    print("=" * 65)

    print(
        f"{'Grand Total':<40}"
        f"{grand_total}"
    )


# ============================================================
# 27. MAIN MENU
# ============================================================

def main():

    while True:

        heading("PYTHON PRACTICE MENU")

        print("1.  Reverse Number")
        print("2.  Digit Sum")
        print("3.  Digit Count")
        print("4.  Perfect Number")
        print("5.  Perfect Number Range")
        print("6.  GCD")
        print("7.  LCM")
        print("8.  Fibonacci")
        print("9.  Second Largest")
        print("10. Second Smallest")
        print("11. Number Frequency")
        print("12. Character Frequency")
        print("13. Word Frequency")
        print("14. Remove Duplicates")
        print("15. Merge Lists")
        print("16. List Intersection")
        print("17. Matrix Addition")
        print("18. Matrix Transpose")
        print("19. Tic Tac Toe")
        print("20. Number Guessing")
        print("21. Rock Paper Scissors")
        print("22. Bank Account")
        print("23. Employee System")
        print("24. Password Validator")
        print("25. Shopping Bill")
        print("26. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            reverse_number()

        elif choice == "2":
            digit_sum()

        elif choice == "3":
            digit_count()

        elif choice == "4":
            perfect_number()

        elif choice == "5":
            perfect_range()

        elif choice == "6":
            gcd_program()

        elif choice == "7":
            lcm_program()

        elif choice == "8":
            fibonacci_list()

        elif choice == "9":
            second_largest()

        elif choice == "10":
            second_smallest()

        elif choice == "11":
            number_frequency()

        elif choice == "12":
            character_frequency()

        elif choice == "13":
            word_frequency()

        elif choice == "14":
            remove_duplicates()

        elif choice == "15":
            merge_lists()

        elif choice == "16":
            list_intersection()

        elif choice == "17":
            matrix_addition()

        elif choice == "18":
            matrix_transpose()

        elif choice == "19":
            tic_tac_toe()

        elif choice == "20":
            guessing_game()

        elif choice == "21":
            rock_paper_scissors()

        elif choice == "22":
            bank_program()

        elif choice == "23":
            employee_system()

        elif choice == "24":
            password_validator()

        elif choice == "25":
            shopping_bill()

        elif choice == "26":

            print("\nPractice complete!")
            print("Keep learning Python 🚀")
            break

        else:

            print("\nInvalid choice.")


# ============================================================
# START
# ============================================================

if __name__ == "__main__":

    main()
