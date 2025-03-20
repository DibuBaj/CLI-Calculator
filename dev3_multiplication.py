def multiply():
    try:
        # Take input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Perform multiplication
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
    
    except ValueError:
        print("Invalid input! Please enter numeric values.")
