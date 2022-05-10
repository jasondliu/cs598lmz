import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)
cmock = CMock(save_matrix=True, double_matrix=True)
# constant definition
LIB_VOIDFUN = FUNTYPE(0)
const_long_int = 1000
# a C function definition
fdef = read_file('./fdef.txt', cumode)
# the Python interface of a C function
mockdef = """
api.fdef.restype = ctypes.c_int
def fdef(a1, a2, a3):
    ret = api.fdef(a1, a2, a3)
    return ret
"""

# mockdef = fdef
# mockdef += '\ndef fdef(a1, a2, a3):\n    return mlc_fdef(a1, a2, a3)\n'
# the mock C code for a C function
icmd = interpreter(cmock, VERSION)
icmd.cmdloop()
constant_def = """
#define AAA 0
#define BBB 1
"""
function_def = []
function_def.append
