import ctypes
# Test ctypes.CFUNCTYPE on llvm().
@ctypes.CFUNCTYPE(None)
def _foo(a):
  return a

@ctypes.CFUNCTYPE(c_int)
def _bar(a, b):
  return a + b

print _foo
print _bar
llvm(_foo)
llvm(_bar)
print _foo
print _bar
print _foo(3)
print _bar(3, 4)
# Test ctypes.WINFUNCTYPE on llvm().
@ctypes.WINFUNCTYPE(c_int, c_int, c_int)
def _wfoo(a, b):
  return a + b

print _wfoo
llvm(_wfoo)
print _wfoo(3, 4)
llvm.run()
