import ctypes
ctypes.cast(pBuffer, ctypes.POINTER(ctypes.c_double)).contents.value
 
#if (type == TYPE_DOUBLE)
#   return *(double*)pBuffer;
#else
#    /* error handling */
#endif




#%% CYTHON

#from cpython.pycapsule cimport PyCapsule_IsValid, PyCapsule_GetPointer
from cpython.pycapsule cimport PyCapsule_New, PyCapsule_Import, PyCapsule_GetName
from libc.stdlib cimport malloc, free
from libc.stdio cimport printf, sprintf
from cpython.ref cimport Py_INCREF, Py_DECREF
from cpython.pycapsule cimport PyCapsule_New
from cpython.py2 cimport PyObject
from libc.string cimport strcpy
from cpython.object cimport PyString_AsString
from libc.stddef cimport size_t
from libc cimport float
from libc.string cimport strcpy

# The py
