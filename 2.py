# Program to print multiplication table

num = int(input("Enter a number: "))

print("Multiplication Table of", num)

for i in range(1, 11):
    result = num * i
    print(num, "x", i, "=", result)

print("Table completed successfully!")
