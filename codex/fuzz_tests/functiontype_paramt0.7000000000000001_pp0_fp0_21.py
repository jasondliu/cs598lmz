from types import FunctionType
list(FunctionType(x, globals(), 'foo') for x in [lambda:None, lambda:None])
#>>> [<function foo.<locals>.<lambda> at 0x7f7d655d0bf8>, <function foo.<locals>.<lambda> at 0x7f7d655d0400>]

from functools import partial
class Test:
 def __init__(self, f, x):
  self.f = f
  self.x = x
 def __call__(self, y):
  return self.f(self.x, y)

Test(lambda x,y: x+y, 1).__name__
#>>> '<lambda>'

from functools import partial
class Test:
 def __init__(self, f, x):
  self.f = partial(f,x)
 def __call__(self, y):
  return self.f(y)

Test(lambda x,y: x+y, 1).__name__
#>>> 'partial'

from functools import partial
class Test:
 def __init__(self,
