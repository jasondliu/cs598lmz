import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
  pass

DEFAULT = object()

class C(object):
  pass


def fun1(a, b=0, *c, **d):
  pass

class A(object):
  def fun1(self, a, b=0, *c, **d):
    pass


@staticmethod
def fun1(a, b=0, *c, **d):
  pass

class B(object):
  @staticmethod
  def fun1(self, a, b=0, *c, **d):
    pass

def fun1(a, b=0, *, c, d=DEFAULT):
  pass

class C(object):
  def fun1(self, a, b=0, *, c, d=DEFAULT):
    pass


@staticmethod
def fun1(a, b=0, *, c, d=DEFAULT):
  pass

class D(object):
  @staticmethod
  def fun1(self, a, b=0, *, c, d=DEFAULT):
    pass


