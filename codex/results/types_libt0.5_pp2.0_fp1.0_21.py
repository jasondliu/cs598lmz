import types
types.MethodType(
    lambda self, x: x + 1,
    None,
    int
)

# %load http://www.python-course.eu/python3_lambda.php
#!/usr/bin/python3
# -*- coding: utf-8 -*-

def f(x):
    return x**2

g = lambda x: x**2

print(f(8))
print(g(8))

print("\n")

print( (lambda x: x**2)(8) )


print("\n")

def make_incrementor (n): return lambda x: x + n
f = make_incrementor(2)
g = make_incrementor(6)
print(f(42), g(42))

print("\n")

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)


print("\n")

def myfunc
