import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double
    z = ctypes.c_double
    __slots__ = ("x", "y", "z")

s = S()
s.x = 10.
s.y = 11.
s.z = 12.

print ctypes.c_char_p(id(s))

print ctypes.pointer(s)._objects["_obj"].offset
print ctypes.pointer(s)._objects
print ctypes.pointer(s)._objects["_obj"]._objects
print ctypes.pointer(s)._objects["_obj"]._objects["x"]
print ctypes.pointer(s)._objects["_obj"]._objects["x"]._objects
print ctypes.pointer(s)._objects["_obj"]._objects["y"]._objects
print ctypes.pointer(s)._objects["_obj"]._objects["z"]._objects
</code>
Output:
<code>&lt;__main__.S object at 0x7f53814d6f
