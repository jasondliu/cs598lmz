import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
  global seen_exception
  #print("enter fun")
  seen_exception = False
  try:
    raise Exception
  except:
    seen_exception = True
  return None
f = fun
try:
  f()
  raise Exception("should have seen an exception")
except:
  if not seen_exception:
    raise Exception("expected exception did not happen")
