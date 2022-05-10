import types
# Test types.FunctionType
class args:
  def meth(self, a, b, c):
    pass
a = args()
print type(args.meth)
print isinstance(args.meth, types.FunctionType)
print isinstance(a.meth, types.FunctionType)
print isinstance(a.meth, types.MethodType)

class CallSoThatThisIsConst:
  def __call__(self, arg):
    return arg + 1
print isinstance(CallSoThatThisIsConst, CallSoThatThisIsConst)
print isinstance(CallSoThatThisIsConst(), CallSoThatThisIsConst)

def func():
  pass
print isinstance(func, types.FunctionType)

# Test the dir() builtin

class A:
  pass
a = A()
print dir() == dir(__builtins__)
print dir(a) == ['__doc__', '__module__']

# Test bytearray
print repr(bytearray('abcd'))
x=bytearray('abcd')
assert 'abcd' in repr
