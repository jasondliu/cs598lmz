import ctypes

class S(ctypes.Structure):
    x = ctypes.Union[ctypes.Union[None, unicode], None, ctypes.Union[ctypes.Union[ctypes.Union[float, unicode], ctypes.Union[None, unicode], ctypes.Union[None, int]], ctypes.Union[unicode, ctypes.Union[long, float], None]]]

def dump_info(t):
    print repr(t)
    print ' doc:', repr(t.__doc__)
    print ' repr:', repr(t.__repr__)
    print ' str:', repr(t.__str__)
    print ' basetype:', t._type_
    print ' flags:', t._flags_

dump_info(S.x)
dump_info(S.x._type_)
dump_info(S.x._type_._type_)
