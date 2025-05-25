
while True:
    try:
        # Enter the 2 numbers to divide
        print("Please enter two numbers to divide:")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Divide the numbers
        result = num1 / num2

        print("Result of division is:", result)
        break  # Exit the loop if division is successful

    except ZeroDivisionError:
        print("Cannot divide by zero! Please enter a non-zero number.")

    except ValueError:
        print("Invalid input! Please enter a valid number.")
