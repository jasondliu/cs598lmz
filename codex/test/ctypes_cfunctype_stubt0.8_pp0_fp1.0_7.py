import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

print(type(fun))
print(fun)
print(fun())

array_type = ctypes.c_wchar * 3
print(array_type)
print(array_type('a', 'b', 'c'))

int_array = (ctypes.c_int * 5)()
print(int_array[:])
for i, e in enumerate(int_array):
    print(i, e)

