import ctypes
# Test ctypes.CField
class CTypesObject(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int),
                ("z", ctypes.c_char_p)]
obj = CTypesObject()
obj.x = 1
obj.y = 2
obj.z = b"abc"
# Copy via the C API, using Python functions from embedded.py
from _embedded import embedded_copy_from_ctypes
newobj = CTypesObject()
embedded_copy_from_ctypes(newobj, obj)
print("newobj.x = {}".format(newobj.x))
print("newobj.y = {}".format(newobj.y))
print("newobj.z = {}".format(newobj.z))

print("obj.z @ {}, {}, {}".format(id(obj.z), hex(id(obj.z)), ctypes.addressof(obj.z)))
print("newobj.z @ {}".format(hex(id(newobj.z))))
```

```
