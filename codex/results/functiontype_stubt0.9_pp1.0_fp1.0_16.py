from types import FunctionType
a = (x for x in [1])
b = (x+y for x,y in [(1,0)])
def c(): pass
d = c
d.__dict__ = {'foo':'bar'}

# They're not equal based on __dict__
print a.__dict__, b.__dict__
# But they have identical __dict__
print a.__dict__ == b.__dict__
# Everything is a type (but not an object)
print type(a), type(b), type(c), type(object())
print isinstance(a, FunctionType), isinstance(b, FunctionType), isinstance(c, FunctionType), isinstance(d, FunctionType)

print type(a) == type(b) == type(c) == type(d)
# no globals
print d.__globals__
# Just self
print [x for x in dir(a) if not x.startswith("__")]
print [x for x in dir(b) if not x.startswith("__")]
print [x for x in dir(c) if not x.startswith
