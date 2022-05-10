from types import FunctionType
list(FunctionType(f.__code__, globals())(1,2,3))

#                           Defining functions

# def funcname(parameters):
#     "function_docstring"
#     function_suite
#     return [expression]

# Above shows the syntax for a function definition. Parameters is optional.
# The first statement of the function_suite may optionally be a string literal
# (docstring). The return statement returns with a value from a function. A
# return statement with no arguments is the same as return None.

# return can be used to end a function. The return statement is not required.
# If the end of a function is reached without executing a return statement,
# the default return value is None.

def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y
print(maximum(2, 3))

# The keyword global can be used to make a variable global.

x = 50
def func():
    global x
    print('x is',
