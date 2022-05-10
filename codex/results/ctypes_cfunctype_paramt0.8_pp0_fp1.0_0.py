import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)
class PyCallable(object):
  def __init__(self,func):
    self.func = func
    self.callable = FUNTYPE(self.func)
  def __call__(self,*args,**kwargs):
    self.func(*args,**kwargs)

def pyfunc(*args,**kwargs):
  callback = kwargs.get("callback", None)
  def pycall(*args):
    callback(*args)
  return PyCallable(pycall)

lib_mylib.pyfunc.restype = ctypes.c_void_p
lib_mylib.pyfunc.argtypes = [FUNTYPE]
</code>

