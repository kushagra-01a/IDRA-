# Simple Calculator (Day 1)

def run_calculator():
    print("=== Simple Python Calculator ===")
    
    # 1. Accept two numbers and convert to numeric type
    # Using float() allows the user to enter decimals as well as whole numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please run the program again and enter numbers only.")
        return

    print("\n=== Results ===")
    
    # 2. Perform arithmetic operations and display using formatted print statements (f-strings)
    print(f"Addition (+): {num1} + {num2} = {num1 + num2}")
    print(f"Subtraction (-): {num1} - {num2} = {num1 - num2}")
    print(f"Multiplication (*): {num1} * {num2} = {num1 * num2}")
    
    # 3. Safe division checks to prevent the program from crashing if the user enters 0
    if num2 != 0:
        print(f"Division (/): {num1} / {num2} = {num1 / num2}")
        print(f"Floor Division (//): {num1} // {num2} = {num1 // num2}")
        print(f"Modulus (%): {num1} % {num2} = {num1 % num2}")
    else:
        print("Division (/): Cannot divide by zero!")
        print("Floor Division (//): Cannot divide by zero!")
        print("Modulus (%): Cannot divide by zero!")
        
    print(f"Exponentiation (**): {num1} ** {num2} = {num1 ** num2}")

# Start the program
if __name__ == "__main__":
    run_calculator()
