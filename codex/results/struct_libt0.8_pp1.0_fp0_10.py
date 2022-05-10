import _struct
import _thread
class py_object(_object):
    def __str__(self):
        return "py:" + _object.__str__(self)
    def __repr__(self):
        return "py:" + _object.__repr__(self)

class py_type(_type):
    def __str__(self):
        return "py:" + _type.__str__(self)
    def __repr__(self):
        return "py:" + _type.__repr__(self)

def _is_py_obj(v):
    return not isinstance(v, py_object) and isinstance(v, _object)
def _wrap(v):
    if isinstance(v, py_object):
        return v
    elif isinstance(v, _object):
        if isinstance(v, _type):
            return py_type(v)
        return py_object(v)
    else:
        return v

def _wrap_all(args):
    return tuple(_wrap(arg) for arg in args)
