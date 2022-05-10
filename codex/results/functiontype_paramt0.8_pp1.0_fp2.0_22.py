from types import FunctionType
list(FunctionType([], []))
class Bar(list):
  def __new__(cls):
    return super(Bar, cls).__new__(cls)
list(FunctionType([], []))
[1, 2, 3] + [4]
(i for i in range(1))
class Sub(object):
  def __init__(self, arg=[]):
    self.arg = arg
s = Sub([lambda: 0])
s.arg
s.arg[0]()
class Sub(object):
  def __init__(self, arg=None):
    self.arg = [] if arg is None else arg
s = Sub([lambda: 0])
s.arg
s.arg[0]()
s = Sub()
s.arg
class Sub(object):
  def __init__(self, arg=[]):
    self.arg = arg
s = Sub([lambda: 0])
s.arg
s.arg[0]()
s.arg += [lambda: 1]
s.arg[1]()
class Sub(object):
  def __init__(self
