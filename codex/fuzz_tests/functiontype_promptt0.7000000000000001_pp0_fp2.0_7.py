import types
# Test types.FunctionType
def f():
    pass
c = types.FunctionType
assert c(f) == f
assert c(f, globals()) == f
assert c(f.func_code, globals()) == f
# assert c(f.func_code, globals(), "f", (),
#          ("def f(): pass\n", "test", 1)) == f
assert c(f.func_code, globals(), "f", (),
         (None, "spam", 1)) == f
# raises TypeError
try:
    c(f.func_code, globals(), "f", (),
      (None, "spam", 1), None)
except TypeError:
    pass
else:
    raise AssertionError
# raises TypeError
try:
    c(f.func_code, globals(), "f", (),
      (None, "spam", 1), None, None)
except TypeError:
    pass
else:
    raise AssertionError
# raises ValueError
try:
    c(f.func_code, globals(), "f", (),
     
