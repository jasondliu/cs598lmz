import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()

#####################################################

# Python 3

# Enter your code here. Read input from STDIN. Print output to STDOUT
import threading

# Tail recursion decorator
def tail_recursion(g):
    """
    This decorator eliminates tail recursion
    """
    def f(*args, **kwargs):
        while 1:
            res = g(*args, **kwargs)
            if not res: break
    return f

@tail_recursion
def factorial(n, acc=1):
    """
    Calculate factorial using tail recursion
    """
    if n == 0:
        return acc
    return factorial(n-1, n*acc)

#print(factorial(5))

def is_prime(n):
    """
    Checks if the number is prime
    """
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
