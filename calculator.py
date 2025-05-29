'''

SIMPLE CALCULATOR

make functions for adding, subtracting, multiplying, and divising

output the answer

expandable: save ans in variable for use after?

'''

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

num1 = float(input("What is the first number? "))
num2 = float(input("What is the second number? "))

program = input("add, sub, mul, div? ")

if program.lower() == "add":
    print(addition(num1, num2))
    
if program.lower() == "sub":
    print(subtraction(num1, num2))
    
if program.lower() == "mul":
    print(multiplication(num1, num2))
    
if program.lower() == "div":
    print(division(num1, num2))