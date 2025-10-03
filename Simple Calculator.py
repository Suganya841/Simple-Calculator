# Simple Calculator in Python 🧮

def calculator():
    print("🧮 Welcome to Simple Calculator!")
    
    # Take user input for numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("❌ Invalid input! Please enter numbers only.")
        return

    # Ask user for operation
    print("Choose operation: +, -, *, /")
    operation = input("Enter operation: ")

    # Perform calculation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("❌ Cannot divide by zero!")
            return
    else:
        print("❌ Invalid operation!")
        return

    print(f"✅ Result: {num1} {operation} {num2} = {result}")

# Run the calculator
calculator()
