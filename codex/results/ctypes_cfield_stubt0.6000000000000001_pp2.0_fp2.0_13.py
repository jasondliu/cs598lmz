import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C:
    def __getattribute__(self, name):
        print('get')
        return super().__getattribute__(name)
    def __setattr__(self, name, value):
        print('set')
        super().__setattr__(name, value)

obj = C()
obj.x = 42
print(obj.x)

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

S._fields_[0] = ctypes.CField('x', ctypes.c_int, 0)

obj = S()
obj.x = 42
print(obj.x)

def get(self):
    print('get')

def set(self, value):
    print('set')

ctypes.CField.__get__ = get
ctypes.CField.__set__ = set

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

obj = S()
obj.x = 42

