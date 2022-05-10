from types import FunctionType
list(FunctionType(code))

# def f(x):
#     return x * 10

# print(f(1))
# print(f(2))

# g = FunctionType(code, globals())
# print(g(1))
# print(g(2))

# print(f.__code__ == g.__code__)

# print(f(1))
# func = FunctionType(f.__code__, globals(), name="f2", argdefs=(10,), closure=(10,))
# print(func(100))
# print(func.__defaults__)
# print(func.__closure__)
