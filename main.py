"""
OrderOfNumbers
"""
# Provide your solution here

no1 = int(input("Enter a first number: "))
no2 = int(input("Enter a second number: "))
no3 = int(input("Enter a third number: "))

if no1 < no2 < no3:
    print("numbers are ascending")
elif no3 < no2 < no1:
    print("numbers are descending")
elif no1 % 2 == 0 and no2 % 2 == 0 and no3 % 2 == 0:
    print("no specific order, but all even")
elif no1 % 2 != 0 and no2 % 2 != 0 and no3 % 2 != 0:
    print("no specific order, but all odd")
else:
    print("no specific order")


"""
SumUp
"""
# Provide your solution here

n1 = int(input("Enter an integer: "))
n2 = int(input("Enter another integer: "))

if n1 <= 0:
    print("The number should be >0.")
elif n2 <= 0:
    print("The number should be >0")
elif n2 <= 0 and n1 <= 0:
    print("Both numbers need to be >0.")
elif n1 >= n2:
    print("The second number must be bigger than the first one.")

for i in range(n1, n2 + 1):
    print(i, end=' ')

