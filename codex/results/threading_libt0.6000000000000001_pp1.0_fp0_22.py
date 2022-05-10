import threading
threading.stack_size(2**27)
import sys
import time
import random

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def main():
    print("Enter the three numbers to perform arithmetic operations")
    a = int(input())
    b = int(input())
    c = int(input())
    print("The sum of a and b is: ", add(a, b))
    print("The difference between a and b is: ", sub(a, b))
    print("The product of a and b is: ", mul(a, b))
    print("The division of a and b is: ", div(a, b))
    print("The sum of b and c is: ", add(b, c))
    print("The difference between b and c is: ", sub(b, c))
    print("The product of b and c is: ", mul(b, c))
   
