import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CField.__get__ = lambda self, instance, owner: instance._objects_.get(self.name)
ctypes.CField.__set__ = lambda self, instance, value: instance._objects_.__setitem__(self.name, value)

class C(ctypes.Structure):
    _objects_ = {}
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

c = C()
c.x = 1
c.y = 2
print c._objects_
print c.x, c.y
</code>

