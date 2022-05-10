gi = (i for i in ())
# Test gi.gi_code

import sys

def f():
    yield 1

def g():
    yield from f()

gi = g().gi_code

print(gi.co_name)
print(gi.co_firstlineno)
print(gi.co_filename)
print(gi.co_flags)
print(gi.co_nlocals)
print(gi.co_stacksize)
print(gi.co_code)
print(gi.co_consts)
print(gi.co_names)
print(gi.co_varnames)
print(gi.co_freevars)
print(gi.co_cellvars)
print(gi.co_lnotab)
print(gi.co_cell2arg)
print(gi.co_zombieframe)

# Test gi.gi_frame

import sys

def f():
    yield 1

def g():
    yield from f()

gi = g().gi_frame

print(gi.f_code.co_name)
print(gi.f_code.
