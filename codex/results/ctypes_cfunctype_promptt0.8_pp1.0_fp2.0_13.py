import ctypes
# Test ctypes.CFUNCTYPE
@cfn(ret=ctypes.c_int, argt=(ctypes.c_int, ctypes.c_int))
def add(a, b):
  return a + b
def test_ctypes_CFUNCTYPE():
  c_add = ctypes.cast(add, ctypes.c_void_p)
  assert c_add.value == add.ctypes_funcptr.value

# Test ctypes.CFUNCTYPE with structs
@cfn(ret=ctypes.c_int, argt=(ctypes.c_int, ctypes.c_int, ctypes.c_int))
def add3(a, b, c):
  return a + b + c

def test_ctypes_CFUNCTYPE_structs():
  def run(b, c):
    @cfn(ret=ctypes.c_int,
         argt=(ctypes.c_int, ctypes.c_int, ctypes.c_int))
    def add3(a, b, c):
      return a + b
