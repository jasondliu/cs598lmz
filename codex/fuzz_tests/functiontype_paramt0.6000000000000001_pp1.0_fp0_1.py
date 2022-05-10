from types import FunctionType
list(FunctionType(lambda: None, {}).__globals__)

# []

# The __globals__ attribute of a function is a dictionary that can be modified to change the function's
# variables

def func(x, y):
    return x + y

func(2, 3)

# 5

func.__globals__['y'] = 5

func(2, 3)

# 7

# The __globals__ attribute can be used to implement a function that can be executed in different environments

def func(x):
    return x + y

func(2)

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: global name 'y' is not defined

func.__globals__['y'] = 2
func(2)

# 4

# The __globals__ attribute can be used to implement a function that can be executed in different environments

def func(x):
    return x + y

func.__globals__['y'] = 2

