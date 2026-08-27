# Program to print numbers from 1 to 10
# and calculate their sum and even/odd numbers

sum = 0

for i in range(1, 11):
    print("Number:", i)                             
        
    if i % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

    sum = sum + i

print("----------------")
print("Total Sum =", sum)
