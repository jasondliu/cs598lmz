import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class MyInt(int):
    pass

class MyLong(long):
    pass

class MyFloat(float):
    pass

class MyComplex(complex):
    pass

class MyStr(str):
    pass

class MyUnicode(unicode):
    pass

class MyTuple(tuple):
    pass

class MyList(list):
    pass

class MyDict(dict):
    pass

class MySet(set):
    pass

class MyFrozenset(frozenset):
    pass

class MySlice(slice):
    pass

class MyXRange(xrange):
    pass

class MyBuffer(buffer):
    pass

class MyMemoryView(memoryview):
    pass

class MyType(type):
    pass

class MyClass(object):
    pass

class MyObject(object):
    pass

class MyEllipsis(Ellipsis):
    pass

class MyNotImplemented(NotImplemented):
    pass

class MyIntType(
