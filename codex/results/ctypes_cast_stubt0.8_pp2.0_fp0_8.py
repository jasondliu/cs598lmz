import ctypes
ctypes.cast(1, ctypes.py_object)
</code>
<code>&lt;class 'ctypes.pythonapi.PyCapsule_Type'&gt;
</code>
which is a memory address.  Note that <code>Py_RETURN_NONE</code> is being called in <code>c_function</code>, meaning that it returns <code>None</code>.
What I would like to do is to implement the following C function:
<code>PyObject* PyCapsule_New(void *pointer, const char *name, PyCapsule_Destructor destructor)
</code>
In Cython, so that it returns <code>None</code> instead of a memory address.
This is what I have tried so far:
<code>%cdef extern from "Python.h":
    void* PyCapsule_New(void* pointer, const char* name, PyCapsule_Destructor destructor)

%%cython

cdef type PyCapsule_Destructor:
    pass

cdef inline void c_function(void *
