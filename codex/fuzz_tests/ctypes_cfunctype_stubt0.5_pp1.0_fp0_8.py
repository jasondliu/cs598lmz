import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("hello")
    return None

# Create a python function object
def pyfun():
    print("hello")
    return None

# Convert the python function object to a python object
pyobj = pyfun.__dict__['__func__']

# Convert the python object to a ctypes object
cobj = ctypes.pythonapi.PyCapsule_New(pyobj, None, None)
# Get the address of the ctypes object
addr = ctypes.pythonapi.PyCapsule_GetPointer(cobj, None)

# Convert the address to a ctypes function
cfun = ctypes.CFUNCTYPE(ctypes.py_object)(addr)

# Call the function
cfun()
</code>
Note: I'm not sure if this is the best way to do this.

