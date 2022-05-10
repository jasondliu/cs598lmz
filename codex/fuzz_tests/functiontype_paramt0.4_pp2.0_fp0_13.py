from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__, argdefs=f.__defaults__, closure=f.__closure__))

# [1, 2, 3]

# https://stackoverflow.com/questions/1769403/understanding-kwargs-in-python
# https://stackoverflow.com/questions/36901/what-does-double-star-asterisk-and-star-asterisk-do-for-parameters

def func(**kwargs):
    print(kwargs)

func(a=1, b=2)

# {'a': 1, 'b': 2}

def func(**kwargs):
    print(kwargs)

func(**{'a':1, 'b':2})

# {'a': 1, 'b': 2}

# https://stackoverflow.com/questions/36901/what-does-double-star-asterisk-and-star-asterisk-do-for-parameters

def func(a, b
