import types
types.FileType

# Define a function
def print_hello():
    print "hello"

type(print_hello) # function
print_hello() # hello

type(print_hello()) # NoneType

# define a function with a parameter
def double(x):
    return x * 2

print double(3) # 6

# define a function with multiple parameters
def power(x,y):
    return x ** y

print power(2,3) # 8

# define a function with default parameters
def power(x,y=2):
    return x ** y

print power(3) # 9
print power(3,3) # 27

# define a function with an arbitrary number of parameters
def sum_all(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print sum_all(1,2,3,4,5) # 15

# define a function with an arbitrary number of keyword parameters
def func(**kwargs):
    for key, value in kwargs.items():
        print "%
