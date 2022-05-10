import sys, threading

def run():
    while True:
        print("\n")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        print("\n")
        choice = int(input("Please enter your choice: "))
        print("\n")

        if choice == 1:
            x = int(input("Enter the first number: "))
            y = int(input("Enter the second number: "))
            print("\n")
            print("The sum is: ", x+y)
            print("\n")
        elif choice == 2:
            x = int(input("Enter the first number: "))
            y = int(input("Enter the second number: "))
            print("\n")
            print("The difference is: ", x-y)
            print("\n")
        elif choice == 3:
            x = int(input("Enter the first number: "))
            y = int(input("Enter the second number: "))
            print
