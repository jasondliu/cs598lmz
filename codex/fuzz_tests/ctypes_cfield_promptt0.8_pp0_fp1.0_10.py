import ctypes
# Test ctypes.CField.__new__: key parameter
#
def test(typ, *args, **kw):
  print(len(args), end=' ')
  try:
    x = typ(*args, **kw)
  except TypeError as e:
    print(e)
  else:
    print(x)

class X(ctypes.Structure):
  _fields_ = [('a', ctypes.c_int), ('b', ctypes.c_int)]
  def __init__(self, a, b):
    self.a = a
    self.b = b

print('X', end=' ')
test(X, 1, 2)
test(X, 3, b=4)
test(X, 5)
test(X, 6, 7, 8)
test(X, 9, b=10, c=11)

class X1(X):
  _pack_ = 1

print('X1', end=' ')
test(X1, 1, 2)
test(X1, 3, b=4)
test(X1, 5)
