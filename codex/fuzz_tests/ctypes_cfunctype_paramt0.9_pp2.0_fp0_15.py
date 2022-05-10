import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p)
def FUN(val):
    return ctypes.cast(ctypes.cast(val, ctypes.c_void_p), FUNTYPE)

_aval = lambda a: [int(v) for v in a]

# create API instances
get_api = m.get_api
load = m.load

load(open('printf.a64').read())

# API calls
INVALID = object()
def set_mem(jj, bytes, datatype=INVALID):
    dt = int(datatype) if datatype is not INVALID else 0
    if (jj.storage == ndarray.NDARRAY_DEVICE and
        dtype.is_uintx(datatype) and not dt == get_api(jj.device).DTYPE_UINT8):
        dtype = get_api(jj.device).TYPE_DTYPE
    if isinstance(bytes, ndarray) and bytes.storage == ndarray.NDARRAY_DEVICE:
        assert bytes.device == jj.
