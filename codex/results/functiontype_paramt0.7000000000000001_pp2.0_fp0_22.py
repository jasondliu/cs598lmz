from types import FunctionType
list(FunctionType(FunctionType.__code__, {}, 'foo').__closure__)

# Verify that a function can be converted back to bytes correctly
import marshal, dis

def f():
    a = 10
    b = 20
    def g():
        return a + b
    return g

#d = f.__code__.co_consts[3]
d = f().__code__
code = marshal.dumps(d)
d2 = marshal.loads(code)

# Verify that the function code is identical
print(d)
print(d2)
print(d == d2)

# Verify that the function code can be disassembled
print(dis.dis(d))

# Verify that __code__ is a read-only attribute of functions
def f(): pass
try:
    f.__code__ = 42
except TypeError:
    pass
else:
    print("failed to raise TypeError assigning to __code__")

# Verify that __code__ is a read-only attribute of methods
class C:
    def m(self): pass
try:

