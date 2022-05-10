import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

f = fun()

type(f)

f.__class__

f.__class__.__name__

type(f) == type(1)

type(f) == type(2)

type(f) == type(fun)

type(f) == FUNTYPE

isinstance(f, FUNTYPE)

class C:
    pass

c = C()

type(c)

#
# isinstance vs issubclass
#

class C:
    pass

class D(C):
    pass

isinstance(D(), C)

issubclass(D, C)

isinstance(C(), C)

issubclass(C, C)

issubclass(C, D)

type(D)

type(C)

class E:
    pass

e = E()

type(E)

type(e)

type(type)

class C:
    pass

type(C)

type(C())

#
# inheritance

