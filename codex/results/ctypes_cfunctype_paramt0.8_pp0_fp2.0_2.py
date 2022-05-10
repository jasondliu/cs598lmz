import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.POINTER(ctypes.c_int),ctypes.POINTER(ctypes.c_int),ctypes.c_int,ctypes.c_int,ctypes.c_int)

#if defined(__GNUC__)
#if defined(__i386__)
#define F_FUNC_SYMBOL  "_Z17BSG_OPTIMIZE_IDXP12bsg_operationPiS1_iib"
#elif defined(__x86_64__)
#define F_FUNC_SYMBOL  "_Z17BSG_OPTIMIZE_IDXP12bsg_operationPiiiiib"
#endif
#else
#define F_FUNC_SYMBOL  "BSG_OPTIMIZE_IDX"
#endif

lib = ctypes.CDLL("./libbsgm.so")
optimize = lib[F_FUNC_SYMBOL]
optimize.argtypes = [ctypes.POINTER(bsg_operation), ctypes.POINTER(ctypes
