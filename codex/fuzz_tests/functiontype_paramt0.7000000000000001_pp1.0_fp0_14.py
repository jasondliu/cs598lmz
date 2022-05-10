from types import FunctionType
list(FunctionType(f.__code__, globals())(5, 10))

# We do not have to explicitly define the function with a return statement.
def f(x, y):
    print(x + y)

f(1, 2)

# In the above, print is Python's equivalent of Lisp's write

# The return statement is used to return a value from a function.
def f(x, y):
    return x + y

# If a function does not have a return statement, the special value None is returned.
def f(x, y):
    print(x + y)

# None is not the same as the number zero, nor an empty string, nor the empty list, nor the value False.
# The interpreter treats None as false in boolean expressions.
print(f(1, 2) == None)

# The return statement can return multiple values as a tuple.
def f(x, y):
    return (x + y, x - y)

print(f(5, 3))

# return without an expression argument returns None.
def f(x, y):
    return
