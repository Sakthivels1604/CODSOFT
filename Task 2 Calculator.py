# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main calculator program
while True:
    # Input from the user
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")
    
    choice = input("Enter your choice: ").lower()

    if choice == 'quit':
        break

    if choice in ('add', 'subtract', 'multiply', 'divide'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        if choice == 'add':
            result = add(num1, num2)
        elif choice == 'subtract':
            result = subtract(num1, num2)
        elif choice == 'multiply':
            result = multiply(num1, num2)
        elif choice == 'divide':
            result = divide(num1, num2)

        print(f"Result: {result}")
    else:
        print("Invalid input. Please enter a valid operation.")
