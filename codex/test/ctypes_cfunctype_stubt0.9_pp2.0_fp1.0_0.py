import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
  return None
class A(object):
  __slots__ = [
    'a',
    ]
  def __getattribute__(self, name):
    pass
  def __setattribute__(self, name, value):
    pass
  def __delattr__(self, name):
    pass
o = A()
o.a = 0
try:
    o.a = 0
except:
    pass
