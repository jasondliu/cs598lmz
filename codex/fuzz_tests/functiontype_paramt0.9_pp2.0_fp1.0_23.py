from types import FunctionType
list(FunctionType(add, globals(), 'add')(4,5))

def twice(func):
    def inner(*args):
        return func(*func(*args))
    return inner
list(twice(add)(4,5))

https://realpython.com/primer-on-python-decorators/
