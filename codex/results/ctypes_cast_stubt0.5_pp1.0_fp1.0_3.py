import ctypes
ctypes.cast(0, ctypes.py_object).value

# This is okay in Cython, but not in Python
# cdef int i = <int>0

# This is okay in Cython, but not in Python
# cdef int i = <int>'a'

# This is okay in Cython, but not in Python
# cdef object o = <object>0

# This is okay in Cython, but not in Python
# cdef object o = <object>'a'

# This is okay in Cython, but not in Python
# cdef str s = <str>0

# This is okay in Cython, but not in Python
# cdef str s = <str>'a'

# This is okay in Cython, but not in Python
# cdef unicode u = <unicode>0

# This is okay in Cython, but not in Python
# cdef unicode u = <unicode>'a'

# This is okay in Cython, but not in Python
# cdef int i = <int>'a'

# This is okay
