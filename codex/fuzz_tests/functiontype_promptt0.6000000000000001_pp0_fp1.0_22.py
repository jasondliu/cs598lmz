import types
# Test types.FunctionType
class A:
  def __init__(self):
    self.x = 1

  @staticmethod
  def f(x):
    return x+1
a = A()
print type(A.f) == types.FunctionType
print A.f(10)
print isinstance(A.f, types.FunctionType)
print a.f(20)
print isinstance(a.f, types.FunctionType)

# Test types.MethodType
class B:
  def __init__(self):
    self.x = 1

  def f(self, x):
    return x+self.x
b = B()
print type(B.f) == types.MethodType
print B.f(b, 10)
print isinstance(B.f, types.MethodType)
print b.f(20)
print isinstance(b.f, types.MethodType)

# Test types.ClassType
class C(object):
  def __init__(self, x):
    self.x = x
print type(C) == types.ClassType
print is
