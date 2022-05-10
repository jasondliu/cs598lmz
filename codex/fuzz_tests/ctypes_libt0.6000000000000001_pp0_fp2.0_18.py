import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Python - Loops")

#define function
def is_even():
    even_numbers = []
    for x in range(1,101):
        if x%2 == 0:
            even_numbers.append(x)
    print(even_numbers)

def is_odd():
    odd_numbers = []
    for x in range(1,101):
        if x%2 == 1:
            odd_numbers.append(x)
    print(odd_numbers)

def is_prime():
    prime_numbers = []
    for x in range(1,101):
        if x > 1:
            for i in range(2,x):
                if (x%i) == 0:
                    break
            else:
                prime_numbers.append(x)
    print(prime_numbers)

def is_palindrome():
    print("Enter the string to check if it is palindrome")
    string_to_check = input()
    string_to_check =
