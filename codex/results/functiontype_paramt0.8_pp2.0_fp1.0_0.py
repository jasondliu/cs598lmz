from types import FunctionType
list(FunctionType(add.__code__, globals(), 'add', add.__defaults__, add.__closure__)())

# class method
def greet(age):
    def wrapper(func):
        def inner(*args):
            return f'{func(*args)}, Your age is {age}'
        return inner
    return wrapper

dec = greet(20)
@dec
def say_hi(name):
    return 'Hi ' + name

say_hi('Lily')


# closure
def outer_func(*args):
    a = 2
    b = 3
    def inner_func(*args):
        # nonlocal a, b
        return a + b
    return inner_func(*args)

# func_args = [1, 2, 3]
# print(outer_func(*func_args))

# generator
def fib(n):
    a, b = 0, 1
    i = 0
    while i < n:
        a, b = b, a + b
        yield a
        i += 1

[x for x in fib(10)]
