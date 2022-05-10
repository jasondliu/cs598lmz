import ctypes
# Test ctypes.CFUNCTYPE.
class Bar:
  pass

def foo(x):
  print x.contents.value
  return 0

BarPtr = ctypes.POINTER(Bar)
BarPtrPtr = ctypes.POINTER(BarPtr)

FOO = ctypes.CFUNCTYPE(ctypes.c_int, BarPtr)
foo_ptr = FOO(foo)

bar = Bar()
bar_ptr = BarPtr(bar)
bar_ptr_ptr = BarPtrPtr(bar_ptr)

foo_ptr(bar_ptr)
foo_ptr(bar_ptr_ptr.contents)
