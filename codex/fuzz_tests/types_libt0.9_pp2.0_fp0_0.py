import types
types.FunctionType(None)
  
def hello():
  print "Hello"
  
type(hello)
isinstance(hello, types.FunctionType)
  
import inspect
inspect.getmembers(hello)
inspect.getargspec(hello)
inspect.isfunction(hello)
inspect.isbuiltin(hello)
inspect.isclass(hello)
  
inspect.getdoc(hello)
inspect.getfile(hello)
inspect.getmodule(hello)
inspect.getsourcefile(hello)
inspect.getsourcelines(hello)
  
inspect.getargspec(hello())
  
'''（4）类定义。 '''
  
class C(object):
  def __init__(self, x):
    self.x = x
    
  def getx(self):
    return self.x
    
type(C)
isinstance(C, type)
inspect.isclass(C)
inspect.isfunction(C)
  
C(10).getx()
