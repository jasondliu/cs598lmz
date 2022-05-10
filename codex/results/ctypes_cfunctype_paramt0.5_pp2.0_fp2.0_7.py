import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def my_callback(a, b):
    print a, b
    return 0
c_callback = FUNTYPE(my_callback)

class MyStruct(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int),
                ('callback', FUNTYPE)]

print ctypes.sizeof(FUNTYPE)
print ctypes.sizeof(MyStruct)

m = MyStruct(1, 2, c_callback)
print m.a, m.b, m.callback(3, 4)
print m.callback(5, 6)
</code>
The output of the above program is:
<code>8
16
1 2 3 4
5 6
</code>

