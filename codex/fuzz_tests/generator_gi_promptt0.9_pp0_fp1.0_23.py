gi = (i for i in ())
# Test gi.gi_code.co_argcount
try:
    gi.gi_code.co_argcount
except AttributeError:
    print('SKIP')
    raise SystemExit


def square(x): return x ** 2


print(gen_func.__code__.co_varnames)
print(list(gen_func(square, 1, 10)))
print(gen_func.__code__.co_varnames)


def foo(x, y, z=1):
    pass


print(foo.__code__.co_varnames)
print(foo.__defaults__)

try:
    foo.__closure__
except AttributeError:
    print('SKIP')
