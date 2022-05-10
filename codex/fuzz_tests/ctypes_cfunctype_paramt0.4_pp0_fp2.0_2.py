import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def _make_cfunc(name):
    return FUNTYPE(('%s_' % name).encode('ascii'))

# _c_erf = _make_cfunc('erf')
# _c_erfc = _make_cfunc('erfc')
_c_erfcx = _make_cfunc('erfcx')
_c_erfi = _make_cfunc('erfi')

# erf = _c_erf
# erfc = _c_erfc
erfcx = _c_erfcx
erfi = _c_erfi
