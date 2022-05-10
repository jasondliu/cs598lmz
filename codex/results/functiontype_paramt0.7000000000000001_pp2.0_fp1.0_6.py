from types import FunctionType
list(FunctionType(lambda: 1).__dict__.keys())

#['__annotations__', '__closure__', '__code__', '__defaults__', '__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']

#In Python 3.5, the __dict__ attribute of a function is a read-only proxy to the underlying locals object.
#The locals object is a dictionary, but it can only be accessed from within the function.

#you can access the __dict__ of the underlying locals object by accessing the __dict__ attribute of the __globals__ attribute of the function.

#Function.__globals__
#The dictionary object that holds the global variables for the module in which the function is defined.

def func():
  a = 1
  b = 2
  return a + b

func.__dict__ = {'new': 'dict'} #Raises an exception, because __dict__ is read-only
func.__globals__['new'] = 'dict'

#This is the same as assigning to the
