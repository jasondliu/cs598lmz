import types
# Test types.FunctionType type.

# Base types to test against.
class Foo(object):
  def __init__(self, x):
    self.x = x

  def GetX(self):
    return self.x

class Bar(Foo):
  pass

class Baz(object):
  def GetX(self):
    return 1

def Test(expected, value):
  result = (type(value) == types.FunctionType)
  if result != expected:
    raise Exception("Unexpected result for %s. %s != %s" %
                    (value, expected, result))

def GetIsEmpty():
  return False

def GetIsNotEmpty():
  a = 1
  return False

def GetFoo():
  return Foo(5)

def GetBar():
  return Bar(5)

def GetBaz():
  return Baz()

def GetFooMethod():
  return Foo(5).GetX

def GetBarMethod():
  return Bar(5).GetX

def GetBazMethod():
  return Baz().GetX


