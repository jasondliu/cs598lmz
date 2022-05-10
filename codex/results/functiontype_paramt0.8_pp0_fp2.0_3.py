from types import FunctionType
list(FunctionType(code, globs=globals()).__closure__)

# There is an alternative syntax for getting closures of nested functions in Python 3.6:
import functools

def adder(x):
    def add(y):
        return x + y
    return add

# This works as expected.
assert adder(5)(10) == 15

# And this will give you the closure.
functools.update_wrapper(adder(5), lambda: None)
# (<cell at 0x10ef11b78: int object at 0xa5f89a0>,)

# In Python 3.6, you can get the closure variable of a function even if the variable has been deleted:
import dis

def adder(x):
    def add(y):
        return x + y
    return add

a = adder(5)
print(dis.dis(a))
# 3           0 LOAD_CLOSURE             0 (x)
#              2 BUILD_TUPLE             1
#              4 LOAD_CONST               1 (<code object add at 0x10
