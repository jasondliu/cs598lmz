import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None
fun()
def fun():
    pass

# Test for Issue #2818:
class Base:
    def __init__(self):
        self.x = 2
        self.y = 3

    def __getitem__(self, key):
        return getattr(self, key)

class Derived(Base):
    def __init__(self):
        self.w = 4
        super(Derived, self).__init__()
