import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Dict(object):
    def __getitem__(self, name):
        return lambda: 1

class C(ctypes.Structure):
    _fields_ = [('foo', ctypes.c_int)]

def constructor(self):
    self.foo = 42

C._fields_ = [('bar', ctypes.c_int),
              ('baz', ctypes.c_int)]

if __name__ == '__main__':
    s = ctypes.Structure

    s._fields_ = [('x', ctypes.c_int),
                  ('y', ctypes.c_int)]

    print s.x
    print s.y

    s._fields_ = [('a', ctypes.c_int),
                  ('b', ctypes.c_int),
                  ('c', ctypes.c_int)]
    print s.a
    print s.b
    print s.c

    s._fields_ = [('t', ctypes.c_int)]
    print s.t

    # print s.x

   
