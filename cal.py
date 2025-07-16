def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculator():
    print("=== Simple Calculator ===")
    while True:
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        print("\nSelect operation:")
        print(" +  Addition")
        print(" -  Subtraction")
        print(" *  Multiplication")
        print(" /  Division")

        operation = input("Enter operation (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Invalid operation. Please choose +, -, *, or /.")

        cont = input("\nDo you want to perform another calculation? (y/n): ").lower()
        if cont != 'y':
            print("Thank you for using the calculator!")
            break
        print("---------------------------")

# Run the calculator
calculator()

