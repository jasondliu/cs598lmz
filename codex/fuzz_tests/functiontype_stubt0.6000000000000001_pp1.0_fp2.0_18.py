from types import FunctionType
a = (x for x in [1])
type(a)

import types
type(a) is types.GeneratorType

import inspect
inspect.isgenerator(a)

print(dir(a))

def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n-1)

factorial(42)

factorial.__doc__

type(factorial)

fact = factorial

fact

fact(5)

map(factorial, range(11))

list(map(fact, range(11)))

factorial.__name__

fact.__name__

funcs = [fact, abs, pow]

funcs

funcs[0]

for f in funcs:
    print(f)

funcs[0](5)

def f3(x):
    return x * x * x

f3

f3(2)

f3(3)

fib = [0, 1, 1, 2, 3, 5, 8, 13,
