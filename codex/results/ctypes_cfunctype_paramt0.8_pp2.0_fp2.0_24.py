import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)
spice.CSPICE_SPKPOS = FUNTYPE(('CSPICE_SPKPOS', spice))
spice.CSPICE_BODVCD = FUNTYPE(('CSPICE_BODVCD', spice))

#get_spice_function = lambda f: ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)(('CSPICE_'+f.upper(), spice))

spice.furnsh(SPICE_KERNELS)#

def get_spice_function(f):
    return ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)(('CSPICE_'+f.upper(), spice))
"""
get_spice_function = lambda f: ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)(('CSPICE_'+f.upper(), spice))

spice.furnsh(SPICE_K
