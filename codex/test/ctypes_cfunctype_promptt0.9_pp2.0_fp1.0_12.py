import ctypes
# Test ctypes.CFUNCTYPE on llvm().
@ctypes.CFUNCTYPE(None)
def _foo(a):
  return a

