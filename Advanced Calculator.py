import math

# Define functions for various operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    return math.sqrt(x)

def factorial(x):
    return math.factorial(x)

def logarithm(x, base=math.e):
    return math.log(x, base)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

# Display menu and process user input
def main():
    print("Welcome to the Advanced Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square root")
    print("7. Factorial")
    print("8. Logarithm")
    print("9. Sine")
    print("10. Cosine")
    print("11. Tangent")
    print("0. Exit")

    choice = None

    while choice != '0':
        choice = input("Enter choice (0-11): ")

        try:
            if choice == '1':
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                print("Result:", add(x, y))

            elif choice == '2':
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                print("Result:", subtract(x, y))

            elif choice == '3':
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                print("Result:", multiply(x, y))

            elif choice == '4':
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                print("Result:", divide(x, y))

            elif choice == '5':
                x = float(input("Enter base number: "))
                y = float(input("Enter exponent number: "))
                print("Result:", power(x, y))

            elif choice == '6':
                x = float(input("Enter number: "))
                print("Result:", sqrt(x))

            elif choice == '7':
                x = int(input("Enter number: "))
                print("Result:", factorial(x))

            elif choice == '8':
                x = float(input("Enter number: "))
                base = float(input("Enter base (default e): ") or math.e)
                print("Result:", logarithm(x, base))

            elif choice == '9':
                x = float(input("Enter number (degrees): "))
                print("Result:", sine(x))

            elif choice == '10':
                x = float(input("Enter number (degrees): "))
                print("Result:", cosine(x))

            elif choice == '11':
                x = float(input("Enter number (degrees): "))
                print("Result:", tangent(x))

            elif choice == '0':
                print("Exiting calculator. Goodbye!")

            else:
                print("Invalid input. Please enter a number between 0 and 11.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
