import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    f = """
 - label
 - label
  text
 - label
""".strip()
    return f

print(fun())


def f(x):
    s = "hello %s" % x
    return s


def f(x, y, z):
    s = "hello %s%s%s" % (x, y, z)
    return s

def f(x, y, z, *a):
    s = "hello %s%s%s%s" % (x, y, z, a)
    return s
