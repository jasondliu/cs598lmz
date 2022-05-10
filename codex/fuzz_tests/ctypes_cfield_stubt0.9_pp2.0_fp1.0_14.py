import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class MyType(int):
    pass

def _f(*args):
    pass

def func():
    s = S()
    s.y = 10
    f = _f
    f.bytes = b'aoeu'
    x = f(1)
    y = x + 1
    b = None
    if b:
        raise 1
    L = [1, 2, 3]
    L[2] = y

    # These could be used to carry the type information to other nodes
    # that depend on the values directly.  The main problem would be
    # that it doesn't come from an annotation, so the annotation code
    # would have to special-case it.
    #b = bytes('aoeuaoeu', 'utf-8')
    #b = bytearray('aoeuaoeu', 'utf-8')

    complexes = [1+2j, 2+3j]
    complexes2 = [complexes[0] + 1j]
    lst = list(complexes.__iter__())
    L.__getitem__
