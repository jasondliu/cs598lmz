from types import FunctionType
list(FunctionType(add,globals()).__globals__)
# returns the name of the function as a list

# Test for annonymus functions:
def double(x):
    return x * 2
lambda x: x * 2
