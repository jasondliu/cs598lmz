from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("i")
s.pack(1)

class T(object):
  pass

t = T()
t.__class__ = Struct
t.__init__("i")
t.pack(1)

class U(Struct):
  pass

u = U("i")
u.pack(1)

class V(object):
  def __init__(self, fmt):
    self.fmt = fmt
  def pack(self, x):
    return Struct(self.fmt).pack(x)

v = V("i")
v.pack(1)

class W(V):
  pass

w = W("i")
w.pack(1)

class X(object):
  def __init__(self, fmt):
    self.fmt = fmt
  def pack(self, x):
    return Struct(self.fmt).pack(x)

class Y(X):
  pass

y = Y("i")
y.pack(1)

class Z(object):
  __sl
