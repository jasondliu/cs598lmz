import ctypes
ctypes.cast(obj, ctypes.py_object).value

# cpdef int func(int x, int y):
#     """Cython doc string"""
#     return x + y
#
# func(1, 2)
#
# cdef int func(int x, int y):
#     """Cython doc string"""
#     return x + y
#
# def run_func(x, y):
#     return func(x,y)
#
# run_func(1, 2)
#
# run_func(1.1, 2.2, 4)
