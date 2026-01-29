# This script performs various mathematical operations on a given number
import math

num = float(input("Enter a number: "))

if num <= 0:
    print("Please enter a positive number for logarithm calculation.")
else:
    print("Square Root:", math.sqrt(num))
    print("Natural Logarithm:", math.log(num))
    print("Sine (in radians):", math.sin(num))
