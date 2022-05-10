import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes._CData_retval_ = None

class C:

    def __getattr__(self, name):
        return name

    def __setattr__(self, name, value):
        self.__dict__[name] = value

# Doesn't fail without this tuple
def f():
    C().__fields_ = (('x', CField),)

for i in range(1000):
    f()

def g():
    C()._fields_ = C().__fields_ = None # Get rid of the problem instance

gc.disable()
for i in range(100):
    g()
</code>

