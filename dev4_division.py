def divide():
    try:
        # Take input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Check for division by zero
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")
    
    except ValueError:
        print("Invalid input! Please enter numeric values.")