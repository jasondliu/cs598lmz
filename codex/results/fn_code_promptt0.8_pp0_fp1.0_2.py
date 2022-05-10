fn = lambda: None
# Test fn.__code__.co_code == 'd\x00\x83\x00\x01\x00'
import dis
dis.dis(fn)

print(fn.__code__.co_varnames)
print(fn.__code__.co_argcount)
print(fn.__code__.co_cellvars)
print("--------------")

# Test: If False:
# co_varnames = ()
# co_argcount = 0
# co_cellvars = ()
def fn():
    if False: pass

import dis
dis.dis(fn)

print(fn.__code__.co_varnames)
print(fn.__code__.co_argcount)
print(fn.__code__.co_cellvars)
print("--------------")

# Test: If True:
# co_varnames = ()
# co_argcount = 0
# co_cellvars = ()
def fn():
    if True: pass

import dis
dis.dis(fn)

print(fn.__code__.co_
