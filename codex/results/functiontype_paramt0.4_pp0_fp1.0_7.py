from types import FunctionType
list(FunctionType(lambda: None, globals(), 'lambda') for i in range(10))

# check if the function is in the list
def isin(x):
    return x in [lambda: None]

# check if the function is in the list
def isin2(x):
    return x in [lambda: None for i in range(10)]

# check if the function is in the list
def isin3(x):
    return x in list(FunctionType(lambda: None, globals(), 'lambda') for i in range(10))

# check if the function is in the list
def isin4(x):
    return x in list(FunctionType(lambda: None, globals(), 'lambda') for i in range(10))

# check if the function is in the list
def isin5(x):
    return x in [FunctionType(lambda: None, globals(), 'lambda') for i in range(10)]

# check if the function is in the list
def isin6(x):
    return x in [FunctionType(lambda: None, globals(), 'lambda')
