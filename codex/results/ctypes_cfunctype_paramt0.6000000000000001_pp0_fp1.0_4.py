import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)
print(FUNTYPE)

def func():
    print('func called')
    return None

f = FUNTYPE(func)
print(f)

f()

# <class 'ctypes.CFUNCTYPE'>
# <ctypes.CFUNCTYPE object at 0x7f0f6c8b7d10>
# func called

#NOTE: Python ctypes cannot be used to create C functions that accept or return PyObject*
#      types.
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
print(FUNTYPE)

def func():
    print('func called')
    return None

f = FUNTYPE(func)
print(f)

try:
    f()
except:
    import sys
    print("Unexpected error:", sys.exc_info()[0])
    # Unexpected error: <type 'exceptions.TypeError'>

# <class 'ctypes.CFUNCTYPE'>
# <ctypes.CFUNCTYPE object at 0x7f0f6
