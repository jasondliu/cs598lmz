gi = (i for i in ())
# Test gi.gi_code

import sys
print(sys.getrefcount(gi))
print(sys.getrefcount(gi))

def g():
    yield 1

gi = g()
print(sys.getrefcount(gi))
print(sys.getrefcount(gi))

print(gi.gi_code.co_filename)

def f1():
    pass

print(f1.__code__.co_filename)

print(gi.gi_code.co_name)

print(f1.__code__.co_name)

print(gi.gi_code.co_varnames)

print(f1.__code__.co_varnames)

print(gi.gi_code.co_argcount)

print(f1.__code__.co_argcount)

def f2(x, y, z=1, *a, **b):
    pass

print(f2.__code__.co_varnames)

print(f2.__code__.co_argcount)

def f3
