import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

fun()

# This is the code that is generated:

#         0 LOAD_GLOBAL              0 (ctypes)
#         3 LOAD_ATTR                1 (CFUNCTYPE)
#         6 LOAD_CONST               1 (2)
#         9 LOAD_CONST               2 ((1,))
#        12 CALL_FUNCTION            1
#        15 STORE_FAST               0 (fun)
#
#     >>   18 LOAD_FAST                0 (fun)
#        21 CALL_FUNCTION            0
#        24 POP_TOP
#        25 LOAD_CONST               0 (None)
#        28 RETURN_VALUE

# This is the code that should be generated:

#         0 LOAD_GLOBAL              0 (ctypes)
#         3 LOAD_ATTR                1 (CFUNCTYPE)
#         6 LOAD_CONST               1 (2)
#         9 LOAD_CONST               2 ((1,))
#        12 CALL_FUNCTION            1

