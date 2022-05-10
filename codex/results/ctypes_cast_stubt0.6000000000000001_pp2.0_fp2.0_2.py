import ctypes
ctypes.cast(add, ctypes.py_object).value

#%%
# Function to add two numbers
def add(a, b):
    return a + b

#%%
# Function to multiply two numbers
def mul(a, b):
    return a * b

#%%
# Function to divide two numbers
def div(a, b):
    return a / b

#%%
# Function to subtract two numbers
def sub(a, b):
    return a - b

#%%
# Function to do exponentiation
def exp(a, b):
    return a ** b

#%%
# Function to do factorial
def fact(a):
    return math.factorial(a)

#%%
# Function to find square root
def sqrt(a):
    return a ** 0.5

#%%
# Function to find cube root
def cbrt(a):
    return a ** (1/3)

#%%
# Function to find square
def square(a):
    return a ** 2

#%%
# Function to find cube
def cube(a):
