import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
s = S()

def callme(field):
    field.__set__(s, 12)
    print s.x

axisfilepath = os.path.join(sys.prefix, 'Lib', 'site-packages', 'numpy', 'core', 'multiarray.so')
axisname = 'PyArray_AxisConverter'
multiarray = ctypes.CDLL(axisfilepath)
getaxis = getattr(multiarray, axisname)
#getaxis.restype = ctypes.c_void_p
if False and sys.version > '2.5':
    res = getaxis(callme, ctypes.CField, 0) 
else:
    def callme_callable(field):
        field.__set__(s, 12)
        print s.x
    res = getaxis(callme_callable, 0)
