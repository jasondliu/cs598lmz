import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,
                          ctypes.c_int, ctypes.POINTER(ctypes.c_int))
lib.CFunction.argtypes = [FUNTYPE]
sum_func = FUNTYPE(lambda n, A: sum(A[i] for i in range(n)))
lib.CFunction(sum_func)

# tuple argument type
lib.CPPClass.argtypes = [ctypes.c_int, ctypes.c_int]

# string arguments
lib.stringArgFunction.argtypes = [ctypes.POINTER(ctypes.c_char)]
lib.stringArgFunction.restype = ctypes.POINTER(ctypes.c_char)


# std::string return
lib.getString.restype = ctypes.c_char_p


# Vector types
lib.vectorIntFunction.argtypes = [np.ctypeslib.ndpointer(dtype=np.int32)]
lib.vectorIntFunction.restype = ctypes.c_int

lib.vectorUnsignedCharFunction.argtypes = [
    np.ctypes
