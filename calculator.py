# BASIC CALCULATOR 
print('A basic calculator that adds,subtracts,divides or multiplies two numbers')

# Get user input and store them in variables
number1 = float(input("Enter first number: "))
operator = input("Enter operator: ")
number2 = float(input("Enter second number: "))

# Checking to see if operator == '+' and calculate
if operator == '+':
    print(f"The answer is {number1 + number2}")

# Checking to see if operator == '-' and calculate
if operator == '-':
    print(f"The answer is {number1 - number2}")

# Checking to see if operator == '*' and calculate
if operator == '*':
    print(f"The answer is {number1 * number2}")

# Checking to see if operator == '/' and calculate
if operator == '/':
    print(f"The answer is {number1 / number2}")

