# Task 1: Basic Mathematical Operations

# Taking input from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Division with error handling
if num2 != 0:
    division = num1 / num2
else:
    division = "Cannot divide by zero"

# Displaying results
print("\nResults:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
