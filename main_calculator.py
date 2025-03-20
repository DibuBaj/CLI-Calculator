# Importing the functions from different calculation files
import dev1_addition
import dev2_subtraction
import dev3_multiplication
import dev4_division

def main():
    while True:
        # Show the menu
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        # Take user input for the operation
        choice = input("Choose an operation (1/2/3/4/5): ")

        if choice == '1':
            dev1_addition.add()  # Call the add function from dev1_addition.py
        elif choice == '2':
            dev2_subtraction.subtract()  # Call the subtract function from dev2_subtraction.py
        elif choice == '3':
            dev3_multiplication.multiply()  # Call the multiply function from dev3_multiplication.py
        elif choice == '4':
            dev4_division.divide()  # Call the divide function from dev4_division.py
        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a valid operation.")

# Run the main function
if __name__ == "__main__":
    main()
