import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

assert fun() == 42

# Test that old-style classes work as expected
class OldStyle:
    pass

assert OldStyle.__name__ == "OldStyle"
assert OldStyle().__class__.__name__ == "OldStyle"
assert OldStyle().__class__.__module__ == __name__

class NewStyle(object):
    pass

assert NewStyle.__name__ == "NewStyle"
assert NewStyle().__class__.__name__ == "NewStyle"
assert NewStyle().__class__.__module__ == __name__

# Test that __metaclass__ works as expected
class Meta(type):
    pass

class MetaClass1(object):
    __metaclass__ = Meta

class MetaClass2(object):
    pass

MetaClass2.__metaclass__ = Meta

