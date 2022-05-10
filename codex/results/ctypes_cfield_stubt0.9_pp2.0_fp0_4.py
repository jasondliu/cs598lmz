import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CFieldPointer = type(S._fields_[0])
ctypes.CFields = type(S._fields_)
ctypes.SimpleCFields = collections.namedtuple('SimpleCFields', ('repeat', 'shape', '_dtype_'))
ctypes.ArrayCFields = collections.namedtuple('ArrayCFields', ('repeat', 'shape', '_dtype_', '_pointer_'))

FArray = np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='C_CONTIGUOUS')
FShape = np.ctypeslib.ndpointer(dtype=np.int32, ndim=1, flags='C_CONTIGUOUS')

numpy_version = int(np.__version__.split('.')[0])

if numpy_version < 1:
    raise RuntimeError('Numpy version '+str(np.__version__)+' < 1.0')
elif numpy_version == 1:
    def isCField(f):
        return type(
