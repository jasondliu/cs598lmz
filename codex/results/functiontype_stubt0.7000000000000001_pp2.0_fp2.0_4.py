from types import FunctionType
a = (x for x in [1])
type(a)

# a)
def coro(f):
    def wrapper(*args):
        return f(*args)
    return wrapper

@coro
def f1():
    print('this is f1')

# b)
def coro2(f):
    def wrapper(*args):
        return f(*args)
    return wrapper

@coro2
def f2():
    print('this is f2')

# c)
def coro3(f):
    def wrapper(*args):
        return f(*args)
    return wrapper

@coro3
def f3():
    print('this is f3')

# d)
def coro4(f):
    def wrapper(*args):
        return f(*args)
    return wrapper

@coro4
def f4():
    print('this is f4')

# e)
def coro5(f):
    def wrapper(*args):
        return f(*args)
    return wrapper

@coro5
def f5():
    print('this is
