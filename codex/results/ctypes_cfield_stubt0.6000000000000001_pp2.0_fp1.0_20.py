import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self):
        self.x = 42

def get_pyobject_from_descr(space, w_type, w_obj, descr):
    if we_are_translated():
        raise ValueError
    if isinstance(descr, interp_fielddescr.W_FieldDescr):
        assert isinstance(w_obj, W_Root)
        return w_obj.getfield(descr)
    elif isinstance(descr, interp_fielddescr.W_CFieldDescr):
        if isinstance(w_obj, W_Root):
            cdata = w_obj.getfield(descr)
            return cdata.convert_to_object(space)
        elif isinstance(w_obj, W_CData):
            return w_obj.convert_to_object(space)
        else:
            cdata = rffi.cast(descr.ctype, w_obj)
            return W_CData(space, cdata, descr.ct
