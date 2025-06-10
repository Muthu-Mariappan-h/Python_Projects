number = int(input("Enter a number:"))
num = number
fact = 1
while num >= 1:
    fact *= num
    num -= 1
print("Factorial of", number, "is:", fact)
