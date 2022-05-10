fn = lambda: None
# Test fn.__code__ == None / fn.__defaults__ is None / fn.__dict__ == {}

def f(): pass
# TypeError: __code__ requires a code object
print(f.__code__)

# TypeError: _x__code__ requires a code object
# print(g.__code__)

# TypeError: __code__ requires a code object
# print(fn.__code__)

# TypeError: _x__code__ requires a code object
# print(f.__code__)

# TypeError: __code__ requires a code object
# print(g.__code__)

# TypeError: _x__code__ requires a code object
# print(fn.__code__)


class X:
  """  """

#   TypeError: __code__ requires a code object
#   print(X.__code__)


class Y:
  def __init__(self):
    pass

# TypeError: _x__code__ requires a code object
# print(Y.__code__)
# print(Y.__init__.__
