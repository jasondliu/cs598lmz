import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test(x):
    print('x:', x)
    setattr(x, '_fields_', [])
    print('x:', x)
    x.name = 'y'
    print('x:', x)
    x.name = 'x'
    print('x:', x)

def main():
    test(S._fields_[0])
    test(S.__dict__['_fields_'][0])
    test(ctypes.CField('x', ctypes.c_int))

if __name__ == '__main__':
    main()
