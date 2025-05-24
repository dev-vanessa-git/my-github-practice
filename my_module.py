# Simple Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# User Interface
def main():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")

    choice = input("Enter choice (1/2): ")

    if choice in ['1', '2']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
        except ValueError:
            print("Please enter valid numbers.")
    else:
        print("Invalid choice. Please select 1 or 2.")

# Run the calculator
main()
