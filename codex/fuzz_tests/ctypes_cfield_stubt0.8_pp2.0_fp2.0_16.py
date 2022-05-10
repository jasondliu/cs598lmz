import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Pt(ctypes.c_int):
    """
    The type of a PyTypeObject's tp_hash field.
    """

special_methods = ("__init__",
                   "__new__",
                   "__repr__",
                   "__cmp__",
                   "__getattr__",
                   "__call__",
                   "__lt__",
                   "__le__",
                   "__gt__",
                   "__ge__",
                   "__eq__",
                   "__ne__",
                   "__add__",
                   "__radd__",
                   "__sub__",
                   "__rsub__",
                   "__mul__",
                   "__rmul__",
                   "__div__",
                   "__rdiv__",
                   "__mod__",
                   "__rmul__",
                   "__pos__",
                   "__neg__",
                   "__pow__",
                   "__abs__",
                   "__str__",
                   "__nonzero__",
                   "__iadd__",
                  
