import ctypes
# Test ctypes.CFUNCTYPE
i = ctypes.c_int.in_dll(ctypes.pythonapi, 'Py_IsInitialized')

if i != 1:
    raise Exception("C api isn't initialized!")

# Test ctypes.py_object
i = ctypes.c_long.in_dll(ctypes.pythonapi, 'PyList_Type')
if id(i.value) != id(list):
    raise Exception("Couldn't create some types, see #1602.")
w = ctypes.c_wchar.in_dll(ctypes.pythonapi, 'PyUnicode_Type')
if id(w.value) != id(unicode):
    raise Exception("Problem with ctypes.c_wchar")

# Test calling a ctypes callback
def func(*args):
    return len(args)
CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.py_object)
cmpfunc = CMPFUNC(func)
lst = [1, 2, 3, 4]
if list.sort(lst, cmp
