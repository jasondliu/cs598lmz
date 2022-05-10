import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return (1,2)
</code>


A:

If you want to call the Python function from a C++ program (as opposed to a Python program), you'll need to include the Python library dynamically, rather than statically. According to http://docs.python.org/c-api/veryhigh.html, "A C program can use the Python/C API to run Python code that is either built into the interpreter or contained in code imported at run time."

