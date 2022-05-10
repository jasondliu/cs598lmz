import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.c_void_p)
def wrapper(func):
  import weakref
  f = ctypes.cast(FUNTYPE(func), ctypes.c_void_p)
  def wrapped(*args):
    data = []
    for a in args:
      data.append(a())
    res = _libso.convert(f, tuple(data))
    def _call():
      return res
    return weakref.ref(_call)
  return wrapped

_libso_test = wrapper(test)
def test_wrapper(*args):
  return _libso_test(*args)

_libso_create_value = wrapper(create_value)
def create_value_wrapper(i):
  return _libso_create_value(i)

EXIST_VALUE = None
class Value(object):
  def __init__(self, i):
    self.i = i

  def __del__(self):
    global EXIST_VALUE
    EXIST_VALUE = self.i

  def __call__(self):
