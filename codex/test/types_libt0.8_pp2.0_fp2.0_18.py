import types
types.X = 1
print(globals()['types'].X)

# There are two ways to access a global variable from within a function. 
# The first is to refer to the variable by name:
def square(x):
    return x ** x

def sum_of_squares(x, y):
    return square(x) + square(y)

# The second way is to declare the variable as global by using the global 
# statement:
def square(x):
    print("integerval:", int(x ** x))
    print("stringval:", str(x ** x))
    print("floatval:", float(x ** x))

def sum_of_squares(x, y):
    return square(x) + square(y)

# The main thing to remember with global variables is that if you change them 
# inside of a function, the change persists when you return to the main program:
def foo():
    global a
    a = 200
    print(a)

# Or, equivalently:
def foo():
    global a
   
