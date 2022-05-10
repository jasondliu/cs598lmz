import ctypes
# Test ctypes.CFUNCTYPE
def call_func(func, args, result_as_int = False):
  result = func(*args)
  if result_as_int:
    if isinstance(result, ctypes._SimpleCData):
      return result.value
    return None
  return result
#
IntType = ctypes.c_int32
FloatType = ctypes.c_float
StrType = ctypes.c_char_p
VoidType = ctypes.c_void_p
#
def SimpleCCall(func, argtypes, restype):
  return ctypes.CFUNCTYPE(restype, *argtypes)(func)
#
def AsInt(obj):
  if isinstance(obj, ctypes._SimpleCData):
    return obj.value
  return None

def AsCharP(obj):
  if isinstance(obj, ctypes._SimpleCData):
    return ctypes.cast(obj, StrType).value
  return obj

def AsVoidP(obj):
  if isinstance(obj, ctypes._SimpleCData):
    return ctypes
