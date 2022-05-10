from types import FunctionType
list(FunctionType(lambda:2,))

# FunctionType is not callable!
try:
    FunctionType(lambda:2)()
except TypeError:
    pass

set(dir(types.FunctionType)).issubset(set(dir(types.BuiltinFunctionType)))

# Although builtin function types can often be created
# out of normal functions...
types.BuiltinFunctionType(enumerate)

def f():
    pass
types.BuiltinFunctionType(f)

# ... it does *not* work with any function
# (for example lambdas)
try:
    types.BuiltinFunctionType(lambda x:x)
except TypeError:
    pass

# FunctionType usually inherits from WrapperDescriptorType
def f():
    pass
type(f)

def g():
    pass

# Implementing __init__ is useless
# it does not change the type of function instances
def f_impl (self, op):
    self.op = op

types.FunctionType.__init__ = f_impl

assert f_impl.op is None
