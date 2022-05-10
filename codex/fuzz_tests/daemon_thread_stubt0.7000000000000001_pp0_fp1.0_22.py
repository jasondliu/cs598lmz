import sys, threading

def run():
    global x
    x = random.randint(1, 100)
    print(x)

def is_prime(n): #checks if a number is prime
    if n == 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

def factorial(n): #calculates the factorial of a number
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n): #calculates the nth number in the fibonacci sequence
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    else: 
        return fibonacci(n-1) + fibonacci(n-2)

def list_file_names(): #lists the files in the current directory
    dir = os.listdir(os.getcwd())
    for i in dir:
        print(i)

def read_file(name): #reads
