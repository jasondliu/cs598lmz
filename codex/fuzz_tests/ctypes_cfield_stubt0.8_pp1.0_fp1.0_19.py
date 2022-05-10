import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

lltype.c_pyobject_ptr = lltype.Ptr(lltype.PyObject)

def convert_struct(S):
    return lltype.Struct('%s_c' % S._name, *[(name, convert_type(TP)) for name, TP in S._flds.items()])

class ConvertResult(object):
    def __init__(self, ll_type, ll_args, ll_result):
        self.ll_type = ll_type
        self.ll_args = ll_args
        self.ll_result = ll_result
        
def convert_type(T):
    if isinstance(T, lltype.LowLevelType):
        return T
    elif isinstance(T, lltype.Primitive):
        if T is lltype.Void:
            return lltype.Void
        else:
            return lltype.Ptr(lltype.Struct('<unnamed>', ('c_value', T)))
    elif isinstance(T, lltype.Ptr):
        return lltype.Ptr(convert_type
