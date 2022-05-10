import ctypes
ctypes.cast(id(len), ctypes.py_object).value

# We can handle the case where a requested attribute does not exist:
def getattr2(obj, attr, default = "def value"):
  return getattr(obj, attr, default)

