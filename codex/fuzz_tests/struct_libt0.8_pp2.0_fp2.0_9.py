import _struct

# This module provides access to some variables used or maintained by the
# interpreter and to functions that interact strongly with the interpreter.
#
# It is always available.

# Memory allocation routines

# Python memory allocator
PyMem_Malloc = _functions.PyMem_Malloc
PyMem_Malloc.restype = c_void_p
PyMem_Malloc.argtypes = [Py_ssize_t]

# NULL-checked Python memory allocator
PyMem_Calloc = _functions.PyMem_Calloc
PyMem_Calloc.restype = c_void_p
PyMem_Calloc.argtypes = [Py_ssize_t]

# Resizable Python memory allocator
PyMem_Realloc = _functions.PyMem_Realloc
PyMem_Realloc.restype = c_void_p
PyMem_Realloc.argtypes = [c_void_p, Py_ssize_t]

# Memcopy using Python memory allocator
PyMem_Memmove = _functions.PyMem_Memmove
PyMem_Memmove.
