import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
print(fun())
</code>
You should still use the <code>ctypes.pythonapi</code> to access the Python C API, not the <code>Py*</code> functions from the <code>ctypes</code> module; the implementation of those is tailored to the implementation of the Python interpreter, not to the interface/ABI. The <code>PyCapsule</code> API does not provide <code>PyCapsule_FromVoidPtr()</code> nor <code>PyCapsule_GetPointer()</code>, but you can use the equivalent functions with a <code>PyCapsule</code> object instead of a string: the <code>PyCapsule</code> object is the name of the capsule you create.
Using the <code>ctypes</code> API to access the C API:
<code>import ctypes
api = ctypes.pythonapi

PyCapsule_Type = ctypes.py_object.in_dll(ctypes, "PyCapsule_Type")

PyCapsule_New = api.PyCapsule_New
