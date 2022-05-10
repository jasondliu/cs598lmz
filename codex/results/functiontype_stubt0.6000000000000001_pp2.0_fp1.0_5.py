from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])
a.__next__()
b.__next__()
next(a)
next(b)
a.__next__()
b.__next__()

def a(x):
    return x+1

def b(x):
    return x+2

# a(1)
# b(1)
# a(2)
# b(2)
# a(3)
# b(3)

def a_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print("{0} has been used: {1}x".format(func.__name__, wrapper.count))
        return res
    wrapper.count = 0
    return wrapper

def b_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print("{0} has been used: {1}x".format(func.__name
