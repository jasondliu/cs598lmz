import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.Structure):
    pass
X._fields_ = [('x', S), ('y', S)]

c = X()
print c.x.x
print c.y.x

r = ctypes.c_wchar_p("hello world")
print r.value

c = ctypes.CDLL(os.path.abspath("hello.so"))
c.returnOne()
c.hello("world")
c.addTwoNumbers(2, 3)

s = ctypes.c_char_p("hello world")
c.passString(s)

# it is different if type is explicitly specified
c = ctypes.CDLL(os.path.abspath("hello.so"))
c.passString(s, ctypes.c_char_p)

class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

pt = Point(1, 2)
c.passStruct(ctypes.byref(pt
