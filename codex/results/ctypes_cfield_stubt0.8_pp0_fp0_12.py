import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    pass
C.c_field = ctypes.CField

def mangle_c_field(obj, name):
    #print 'mangling', obj, name
    field = getattr(obj, name)
    if isinstance(field, ctypes.CField):
        return 'x_%s_%x' % (name, id(obj))
mangle_c_field._annspecialcase_ = 'specialize:memo'

def mangle(obj, name):
    if name == 'c_field':
        return mangle_c_field(obj, name)

def f(s):
    return s.x

def main(n):
    s = S()
    total = 0
    for i in range(n):
        total += f(s)
    return total

def target(*args):
    return main, None

if __name__ == '__main__':
    import sys
    main(int(sys.argv[1]))
