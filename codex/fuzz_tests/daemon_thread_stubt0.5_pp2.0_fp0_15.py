import sys, threading

def run():
    while 1:
        print("\n[1] Addition")
        print("[2] Subtraction")
        print("[3] Multiplication")
        print("[4] Division")
        print("[5] Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            a = float(input("\nEnter first number: "))
            b = float(input("Enter second number: "))
            print("\n{} + {} = {}".format(a, b, a+b))

        elif choice == '2':
            a = float(input("\nEnter first number: "))
            b = float(input("Enter second number: "))
            print("\n{} - {} = {}".format(a, b, a-b))

        elif choice == '3':
            a = float(input("\nEnter first number: "))
            b = float(input("Enter second number: "))
            print("\n{} * {} = {}".format(a, b, a*b))
