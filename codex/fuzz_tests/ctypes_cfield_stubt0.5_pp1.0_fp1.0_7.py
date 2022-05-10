import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class E(Exception):
    pass

def test(x):
    print type(x)
    if isinstance(x, ctypes.CField):
        raise E
    return x

if __name__ == '__main__':
    import os
    print os.path.abspath('.')
    print os.getcwd()
    print os.path.abspath(os.path.dirname(__file__))
    print os.path.abspath(os.path.dirname(__file__) + '/../')
    print os.path.abspath(os.path.dirname(__file__) + '/../..')
    print repr(os.path.abspath(os.path.dirname(__file__) + '/../..'))
    print repr(os.path.abspath(os.path.dirname(__file__) + '/../../'))
    print repr(os.path.abspath(os.path.dirname(__file__) + '/../../../'))
