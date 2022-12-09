import math

import random


def calculator():
    # Contains the current version of the calculator

    calculator_version = "1.1"

    # Displays options for the user

    def options():

        print("\nOptions")

        print("Enter 'add' to add two numbers")

        print("Enter 'subtract' to subtract two numbers")

        print("Enter 'multiply' to multiply two numbers")

        print("Enter 'divide to divide two numbers")

        print("Enter 'more' to see  a list of more operations available")

        print("Enter 'quit' to end the program")

    options()

    # Allows calculator to be used

    while True:

        user_input = input("\nPlease input your command:")

        # Displays options again for the user

        if user_input == "options":

            pass

        # Displays a list of more operations

        elif user_input == "more":

            print("\nList of more operations")

            print("Enter 'powers' to raise a number to the power of another")

            print("Enter 'sqrt' to find the square root of a number")

            print("Enter 'percent' to calculate percentage of a number")

            print("Enter 'pi' to return value for pi")

            print("Enter 'e' to return value for e")

            print("Enter 'sin' to find sine of a number")

            print("Enter 'cos' to find cosine of a number")

            print("Enter 'tan' to find tangent of a number")

            print("Enter 'rand' to return a random number between 0 and 1")

            print("Enter 'randint' to return a random number between two numbers")

            print("Enter 'radian' to return value for  'degree'")

            print("Enter 'degrees' to return value for  'radian'")

            print("Enter 'arc cosine' to Return the arc cosine of x, in radians")

            print("Enter 'arc sine' to Return the arc sine of x, in radians")

            print("Enter 'arc tangent' to Return the arc tangent of x, in radians")

            print("tangent")

            continue

        # Exits the user from the calculator

        elif user_input == "quit":

            print("\nThank you for using this calculator " + Name + "!")

            break

        # Adds two numbers

        elif user_input == "add":

            try:

                num1 = float(input("Enter the first number:"))

                num2 = float(input("Enter the second number:"))

                result = str(num1 + num2)

                print("\nThe answer is " + result)

            except (ValueError, TypeError):

                print("Error occurred")

        # Subtracts two numbers

        elif user_input == "subtract":

            try:

                num1 = float(input("Enter the first number:"))

                num2 = float(input("Enter the second number:"))

                result = str(num1 - num2)

                print("\nThe answer is " + result)

            except (ValueError, TypeError):

                print("Error occurred")

        # Multiplies two numbers

        elif user_input == "multiply":

            try:

                num1 = float(input("Enter the first number:"))

                num2 = float(input("Enter the second number:"))

                result = str(num1 * num2)

                print("\nThe answer is " + result)

            except (ValueError, TypeError):

                print("Error occurred")

        # Divides two numbers

        elif user_input == "divide":

            try:

                num1 = float(input("Enter the first number:"))

                num2 = float(input("Enter the second number:"))

                result = str(num1 / num2)

                print("\nThe answer is " + result)

            except ZeroDivisionError:

                print("An error has occurred due to zero division")

            except (ValueError, TypeError):

                print("Error occurred")

        # Raises a number to the power of another

        elif user_input == "powers":

            try:

                num1 = float(input("Enter the first number:"))

                num2 = float(input("Enter the second number:"))

                result = str(num1 ** num2)

                print("\nThe answer is " + result)

            except (ValueError, TypeError):

                print("Error occurred")

        # Finds the square root of a number

        elif user_input == "sqrt":

            try:

                num1 = float(input("Enter a number:"))

                result = str(math.sqrt(num1))

                print("\nThe answer is " + result)

            except (ValueError, TypeError):

                print("Error occurred")

        # Calculates percentage of a number

        elif user_input == "percent":

            try:

                num1 = float(input("Enter a number:"))

                result = str(num1 / 100)

                print("\nThe answer is " + result)

            except (ValueError, TypeError):

                print("Error occurred")

        # Returns value for pi

        elif user_input == "pi":

            result = str(math.pi)

            print("\nThe answer is " + result)

        # Returns value for e

        elif user_input == "e":

            result = str(math.e)

            print("\nThe answer is " + result)

        # Finds the sine of a number

        elif user_input == "sin":

            try:

                num1 = float(input("Enter a number:"))

                result = str(math.sin(num1))

                print("\nThe answer is " + result)

            except (ValueError, TypeError):

                print("Error occurred")

        # Finds the cosine of a number

        elif user_input == "cos":

            try:

                num1 = float(input("Enter a number:"))

                result = str(math.cos(num1))

                print("\nThe answer is " + result)

            except (ValueError, TypeError):

                print("Error occurred")

        # Finds the tangent of a number

        elif user_input == "tan":

            try:

                num1 = float(input("Enter a number:"))

                result = str(math.tan(num1))

                print("\nThe answer is " + result)

            except (ValueError, TypeError):

                print("Error occurred")

        # addons
        elif user_input == "radian":

            try:

                num1 = float(input("Enter a number:"))

                result = str(math.degrees(num1))

                print("\nThe answer is " + result)

            except (ValueError, TypeError):

                print("Error occurred")


        elif user_input == "degrees":

            try:

                num1 = float(input("Enter a number:"))

                result = str(math.radians(num1))

                print("\nThe answer is " + result)

            except (ValueError, TypeError):

                print("Error occurred")


        elif user_input == "arc cosine":

            try:

                num1 = float(input("Enter a number:"))

                result = str(math.acos(num1))

                print("\nThe answer is " + result)

            except (ValueError, TypeError):

                print("Error occurred")


        elif user_input == "arc sine":

            try:

                num1 = float(input("Enter a number:"))

                result = str(math.asin(num1))

                print("\nThe answer is " + result)

            except (ValueError, TypeError):

                print("Error occurred")


        elif user_input == "arc tangent":

            try:

                num1 = float(input("Enter a number:"))

                result = str(math.atan(num1))

                print("\nThe answer is " + result)

            except (ValueError, TypeError):

                print("Error occurred")




        # Returns a random number between 0 and 1

        elif user_input == "rand":

            result = str(random.random())

            print("\nThe answer is " + result)

        # Returns a random number between two numbers

        elif user_input == "randint":

            try:

                num1 = float(input("Enter the first number:"))

                num2 = float(input("Enter the second number:"))

                result = str(random.randint(num1, num2))

                print("\nThe answer is " + result)

            except (ValueError, TypeError):

                print("An error occurred")

        # Is displayed when an unknown input is entered
        else:

            print("Unknown input")

        # Displays the options for the user

        options()


# Runs the calculator

calculator() 