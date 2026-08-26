# ============================================================
#                 PYTHON PRACTICE CODE - 6
# ============================================================

import random
import math


# ============================================================
# 1. BASIC HELPER
# ============================================================

def heading(text):
    print("\n" + "=" * 60)
    print(text.center(60))
    print("=" * 60)


# ============================================================
# 2. SWAP TWO NUMBERS
# ============================================================

def swap_numbers():

    heading("SWAP NUMBERS")

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Before swap:")
    print("A =", a)
    print("B =", b)

    a, b = b, a

    print("\nAfter swap:")
    print("A =", a)
    print("B =", b)


# ============================================================
# 3. LARGEST OF THREE
# ============================================================

def largest_three():

    heading("LARGEST OF THREE")

    a = float(input("Enter A: "))
    b = float(input("Enter B: "))
    c = float(input("Enter C: "))

    if a >= b and a >= c:
        largest = a

    elif b >= a and b >= c:
        largest = b

    else:
        largest = c

    print("Largest:", largest)


# ============================================================
# 4. SMALLEST OF THREE
# ============================================================

def smallest_three():

    heading("SMALLEST OF THREE")

    a = float(input("Enter A: "))
    b = float(input("Enter B: "))
    c = float(input("Enter C: "))

    if a <= b and a <= c:
        smallest = a

    elif b <= a and b <= c:
        smallest = b

    else:
        smallest = c

    print("Smallest:", smallest)


# ============================================================
# 5. LEAP YEAR
# ============================================================

def leap_year():

    heading("LEAP YEAR")

    year = int(input("Enter year: "))

    if year % 400 == 0:

        print("Leap year")

    elif year % 100 == 0:

        print("Not a leap year")

    elif year % 4 == 0:

        print("Leap year")

    else:

        print("Not a leap year")


# ============================================================
# 6. COUNT DIGITS
# ============================================================

def count_digits():

    heading("COUNT DIGITS")

    number = abs(
        int(input("Enter number: "))
    )

    if number == 0:

        print("Digits:", 1)
        return

    count = 0

    while number:

        count += 1
        number //= 10

    print("Digits:", count)


# ============================================================
# 7. SUM OF DIGITS
# ============================================================

def sum_digits():

    heading("SUM OF DIGITS")

    number = abs(
        int(input("Enter number: "))
    )

    total = 0

    while number:

        total += number % 10

        number //= 10

    print("Digit sum:", total)


# ============================================================
# 8. MULTIPLICATION TABLES
# ============================================================

def all_tables():

    heading("MULTIPLICATION TABLES")

    for number in range(1, 11):

        print("\nTable of", number)

        for i in range(1, 11):

            print(
                number,
                "x",
                i,
                "=",
                number * i
            )


# ============================================================
# 9. SUM OF EVEN NUMBERS
# ============================================================

def even_sum():

    heading("EVEN NUMBER SUM")

    start = int(input("Start: "))
    end = int(input("End: "))

    total = 0

    for number in range(start, end + 1):

        if number % 2 == 0:

            total += number

    print("Sum of even numbers:", total)


# ============================================================
# 10. SUM OF ODD NUMBERS
# ============================================================

def odd_sum():

    heading("ODD NUMBER SUM")

    start = int(input("Start: "))
    end = int(input("End: "))

    total = 0

    for number in range(start, end + 1):

        if number % 2 != 0:

            total += number

    print("Sum of odd numbers:", total)


# ============================================================
# 11. PRIME CHECK
# ============================================================

def prime_check():

    heading("PRIME CHECK")

    number = int(input("Enter number: "))

    if number < 2:

        print("Not prime")
        return

    for i in range(2, int(math.sqrt(number)) + 1):

        if number % i == 0:

            print("Not prime")
            return

    print("Prime number")


# ============================================================
# 12. PRIME RANGE
# ============================================================

def prime_range():

    heading("PRIME RANGE")

    start = int(input("Start: "))
    end = int(input("End: "))

    print("Prime numbers:")

    for number in range(start, end + 1):

        if number < 2:
            continue

        prime = True

        for i in range(2, int(math.sqrt(number)) + 1):

            if number % i == 0:

                prime = False
                break

        if prime:

            print(number, end=" ")

    print()


# ============================================================
# 13. PALINDROME NUMBER
# ============================================================

def palindrome_number():

    heading("PALINDROME NUMBER")

    number = input("Enter number: ")

    if number == number[::-1]:

        print("Palindrome")

    else:

        print("Not palindrome")


# ============================================================
# 14. PALINDROME STRING
# ============================================================

def palindrome_string():

    heading("PALINDROME STRING")

    text = input("Enter text: ")

    text = text.lower().replace(" ", "")

    if text == text[::-1]:

        print("Palindrome")

    else:

        print("Not palindrome")


# ============================================================
# 15. ARMSTRONG
# ============================================================

def armstrong():

    heading("ARMSTRONG NUMBER")

    number = int(input("Enter number: "))

    original = number

    digits = len(str(number))

    total = 0

    while number:

        digit = number % 10

        total += digit ** digits

        number //= 10

    if total == original:

        print("Armstrong number")

    else:

        print("Not Armstrong")


# ============================================================
# 16. FACTORIAL
# ============================================================

def factorial():

    heading("FACTORIAL")

    number = int(input("Enter number: "))

    if number < 0:

        print("Invalid number")
        return

    result = 1

    for i in range(1, number + 1):

        result *= i

    print("Factorial:", result)


# ============================================================
# 17. FIBONACCI
# ============================================================

def fibonacci():

    heading("FIBONACCI")

    count = int(
        input("Number of terms: ")
    )

    a = 0
    b = 1

    for _ in range(count):

        print(a, end=" ")

        a, b = b, a + b

    print()


# ============================================================
# 18. STAR PATTERN
# ============================================================

def star_pattern():

    heading("STAR PATTERN")

    rows = int(input("Rows: "))

    for i in range(1, rows + 1):

        print("* " * i)


# ============================================================
# 19. REVERSE STAR PATTERN
# ============================================================

def reverse_star_pattern():

    heading("REVERSE STAR PATTERN")

    rows = int(input("Rows: "))

    for i in range(rows, 0, -1):

        print("* " * i)


# ============================================================
# 20. PYRAMID
# ============================================================

def pyramid():

    heading("PYRAMID")

    rows = int(input("Rows: "))

    for i in range(1, rows + 1):

        spaces = " " * (rows - i)

        stars = "* " * i

        print(spaces + stars)


# ============================================================
# 21. NUMBER PATTERN
# ============================================================

def number_pattern():

    heading("NUMBER PATTERN")

    rows = int(input("Rows: "))

    for i in range(1, rows + 1):

        for j in range(1, i + 1):

            print(j, end=" ")

        print()


# ============================================================
# 22. REVERSE NUMBER PATTERN
# ============================================================

def reverse_number_pattern():

    heading("REVERSE NUMBER PATTERN")

    rows = int(input("Rows: "))

    for i in range(rows, 0, -1):

        for j in range(1, i + 1):

            print(j, end=" ")

        print()


# ============================================================
# 23. LIST INPUT
# ============================================================

def list_input():

    heading("LIST INPUT")

    numbers = []

    count = int(
        input("How many numbers? ")
    )

    for i in range(count):

        value = int(
            input(
                f"Number {i + 1}: "
            )
        )

        numbers.append(value)

    print("\nList:", numbers)

    print("Sum:", sum(numbers))
    print("Max:", max(numbers))
    print("Min:", min(numbers))

    if numbers:

        print(
            "Average:",
            sum(numbers) / len(numbers)
        )


# ============================================================
# 24. EVEN AND ODD LISTS
# ============================================================

def separate_list():

    heading("SEPARATE EVEN AND ODD")

    numbers = [
        1, 4, 7, 10, 13,
        16, 21, 24, 30
    ]

    even = []
    odd = []

    for number in numbers:

        if number % 2 == 0:

            even.append(number)

        else:

            odd.append(number)

    print("Original:", numbers)
    print("Even:", even)
    print("Odd:", odd)


# ============================================================
# 25. MAX WITHOUT MAX()
# ============================================================

def maximum_without_function():

    heading("MAX WITHOUT MAX()")

    numbers = [
        12, 45, 67,
        23, 89, 34,
        90, 56
    ]

    largest = numbers[0]

    for number in numbers[1:]:

        if number > largest:

            largest = number

    print("Numbers:", numbers)
    print("Largest:", largest)


# ============================================================
# 26. MIN WITHOUT MIN()
# ============================================================

def minimum_without_function():

    heading("MIN WITHOUT MIN()")

    numbers = [
        12, 45, 67,
        23, 89, 34,
        90, 5
    ]

    smallest = numbers[0]

    for number in numbers[1:]:

        if number < smallest:

            smallest = number

    print("Numbers:", numbers)
    print("Smallest:", smallest)


# ============================================================
# 27. REMOVE DUPLICATES
# ============================================================

def remove_duplicates():

    heading("REMOVE DUPLICATES")

    numbers = [
        10, 20, 10,
        30, 40, 20,
        50, 30, 60
    ]

    result = []

    for number in numbers:

        if number not in result:

            result.append(number)

    print("Original:", numbers)
    print("Unique:", result)


# ============================================================
# 28. LIST ROTATION
# ============================================================

def list_rotation():

    heading("LIST ROTATION")

    numbers = [
        1, 2, 3,
        4, 5, 6
    ]

    positions = int(
        input("Rotate by: ")
    )

    positions %= len(numbers)

    result = (
        numbers[-positions:]
        + numbers[:-positions]
    )

    print("Original:", numbers)
    print("Rotated:", result)


# ============================================================
# 29. DICTIONARY STUDENTS
# ============================================================

def dictionary_students():

    heading("STUDENT DICTIONARY")

    students = {}

    count = int(
        input("Number of students: ")
    )

    for i in range(count):

        name = input("Name: ")

        marks = float(
            input("Marks: ")
        )

        students[name] = marks

    print("\nStudents:")

    for name, marks in students.items():

        print(
            name,
            "=>",
            marks
        )


# ============================================================
# 30. FIND TOP STUDENT
# ============================================================

def top_student():

    heading("TOP STUDENT")

    students = {
        "Rahul": 85,
        "Aman": 91,
        "Priya": 88,
        "Rohit": 76,
        "Neha": 95
    }

    top_name = None
    top_marks = -1

    for name, marks in students.items():

        if marks > top_marks:

            top_marks = marks
            top_name = name

    print("Top student:", top_name)
    print("Marks:", top_marks)


# ============================================================
# 31. WORD LENGTH DICTIONARY
# ============================================================

def word_length():

    heading("WORD LENGTH")

    sentence = input(
        "Enter sentence: "
    )

    words = sentence.split()

    result = {}

    for word in words:

        result[word] = len(word)

    for word, length in result.items():

        print(
            word,
            "=>",
            length
        )


# ============================================================
# 32. SIMPLE LOGIN
# ============================================================

def login_system():

    heading("LOGIN SYSTEM")

    correct_username = "admin"
    correct_password = "python123"

    attempts = 3

    while attempts > 0:

        username = input(
            "Username: "
        )

        password = input(
            "Password: "
        )

        if (
            username == correct_username
            and password == correct_password
        ):

            print("Login successful!")
            return

        attempts -= 1

        print(
            "Wrong credentials.",
            attempts,
            "attempts left."
        )

    print("Account locked.")


# ============================================================
# 33. NUMBER GUESSING GAME
# ============================================================

def guessing_game():

    heading("GUESSING GAME")

    secret = random.randint(1, 50)

    attempts = 0

    while True:

        try:

            guess = int(
                input("Guess 1-50: ")
            )

            attempts += 1

            if guess < secret:

                print("Too low!")

            elif guess > secret:

                print("Too high!")

            else:

                print(
                    "Correct!",
                    "Attempts:",
                    attempts
                )

                break

        except ValueError:

            print("Enter a number.")


# ============================================================
# 34. ROCK PAPER SCISSORS
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

    for round_number in range(5):

        print(
            "\nRound",
            round_number + 1
        )

        player = input(
            "Choose: "
        ).lower()

        if player not in choices:

            print("Invalid.")
            continue

        computer = random.choice(
            choices
        )

        print(
            "Computer:",
            computer
        )

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

    print("\nPlayer:", player_score)
    print("Computer:", computer_score)


# ============================================================
# 35. ATM CLASS
# ============================================================

class ATM:

    def __init__(self):

        self.balance = 10000

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

        print(
            "Balance:",
            self.balance
        )


# ============================================================
# 36. ATM PROGRAM
# ============================================================

def atm_program():

    heading("ATM")

    atm = ATM()

    pin = "1234"

    attempts = 3

    while attempts > 0:

        entered = input(
            "Enter PIN: "
        )

        if entered == pin:

            print("Welcome!")
            break

        attempts -= 1

        print(
            "Wrong PIN."
        )

    else:

        print("Card blocked.")
        return

    while True:

        print("\n1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choice: ")

        try:

            if choice == "1":

                atm.show_balance()

            elif choice == "2":

                amount = float(
                    input("Amount: ")
                )

                atm.deposit(amount)

            elif choice == "3":

                amount = float(
                    input("Amount: ")
                )

                atm.withdraw(amount)

            elif choice == "4":

                break

            else:

                print("Invalid.")

        except ValueError:

            print("Enter valid amount.")


# ============================================================
# 37. TIC TAC TOE
# ============================================================

def tic_tac_toe():

    heading("TIC TAC TOE")

    board = [
        "1", "2", "3",
        "4", "5", "6",
        "7", "8", "9"
    ]

    player = "X"

    winning_patterns = [

        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),

        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),

        (0, 4, 8),
        (2, 4, 6)

    ]

    for turn in range(9):

        print()

        print(
            board[0],
            "|",
            board[1],
            "|",
            board[2]
        )

        print("--+---+--")

        print(
            board[3],
            "|",
            board[4],
            "|",
            board[5]
        )

        print("--+---+--")

        print(
            board[6],
            "|",
            board[7],
            "|",
            board[8]
        )

        try:

            position = int(
                input(
                    f"\nPlayer {player}, "
                    "choose 1-9: "
                )
            ) - 1

            if position < 0 or position > 8:

                print("Invalid.")
                continue

            if board[position] in ["X", "O"]:

                print("Already occupied.")
                continue

            board[position] = player

        except ValueError:

            print("Enter number.")
            continue

        won = False

        for a, b, c in winning_patterns:

            if (
                board[a] == player
                and board[b] == player
                and board[c] == player
            ):

                won = True
                break

        if won:

            print(
                f"\nPlayer {player} wins!"
            )

            return

        if player == "X":

            player = "O"

        else:

            player = "X"

    print("\nGame Draw!")


# ============================================================
# 38. MAIN MENU
# ============================================================

def main():

    while True:

        heading("PYTHON PRACTICE - 6")

        print("1.  Swap Numbers")
        print("2.  Largest of Three")
        print("3.  Smallest of Three")
        print("4.  Leap Year")
        print("5.  Count Digits")
        print("6.  Sum of Digits")
        print("7.  All Tables")
        print("8.  Even Sum")
        print("9.  Odd Sum")
        print("10. Prime Check")
        print("11. Prime Range")
        print("12. Palindrome Number")
        print("13. Palindrome String")
        print("14. Armstrong")
        print("15. Factorial")
        print("16. Fibonacci")
        print("17. Star Pattern")
        print("18. Reverse Star Pattern")
        print("19. Pyramid")
        print("20. Number Pattern")
        print("21. Reverse Number Pattern")
        print("22. List Input")
        print("23. Separate Even/Odd")
        print("24. Max Without max()")
        print("25. Min Without min()")
        print("26. Remove Duplicates")
        print("27. List Rotation")
        print("28. Student Dictionary")
        print("29. Top Student")
        print("30. Word Length")
        print("31. Login System")
        print("32. Guessing Game")
        print("33. Rock Paper Scissors")
        print("34. ATM")
        print("35. Tic Tac Toe")
        print("36. Exit")

        choice = input(
            "\nEnter choice: "
        )

        if choice == "1":
            swap_numbers()

        elif choice == "2":
            largest_three()

        elif choice == "3":
            smallest_three()

        elif choice == "4":
            leap_year()

        elif choice == "5":
            count_digits()

        elif choice == "6":
            sum_digits()

        elif choice == "7":
            all_tables()

        elif choice == "8":
            even_sum()

        elif choice == "9":
            odd_sum()

        elif choice == "10":
            prime_check()

        elif choice == "11":
            prime_range()

        elif choice == "12":
            palindrome_number()

        elif choice == "13":
            palindrome_string()

        elif choice == "14":
            armstrong()

        elif choice == "15":
            factorial()

        elif choice == "16":
            fibonacci()

        elif choice == "17":
            star_pattern()

        elif choice == "18":
            reverse_star_pattern()

        elif choice == "19":
            pyramid()

        elif choice == "20":
            number_pattern()

        elif choice == "21":
            reverse_number_pattern()

        elif choice == "22":
            list_input()

        elif choice == "23":
            separate_list()

        elif choice == "24":
            maximum_without_function()

        elif choice == "25":
            minimum_without_function()

        elif choice == "26":
            remove_duplicates()

        elif choice == "27":
            list_rotation()

        elif choice == "28":
            dictionary_students()

        elif choice == "29":
            top_student()

        elif choice == "30":
            word_length()

        elif choice == "31":
            login_system()

        elif choice == "32":
            guessing_game()

        elif choice == "33":
            rock_paper_scissors()

        elif choice == "34":
            atm_program()

        elif choice == "35":
            tic_tac_toe()

        elif choice == "36":

            print(
                "\nPractice complete! 🚀"
            )

            break

        else:

            print(
                "\nInvalid choice."
            )


# ============================================================
# START PROGRAM
# ============================================================

if __name__ == "__main__":

    main()
