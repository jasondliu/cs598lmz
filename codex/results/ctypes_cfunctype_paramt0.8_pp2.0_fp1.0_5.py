import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)

LIBSPEC = './rlib/libR.so'


class RPyException(Exception):
    pass


class RInterface(object):
    def __init__(self, libR, R_P_ACTIVE_BINDING, R_P_METHOD_DISPATCH, R_P_METHOD_LOOKUP, R_P_SET_ACTIVE_BINDING, R_P_SET_CLASS, R_P_SET_OBJECT, R_P_SET_VECTOR, R_DispatchOrEval, Rf_eval, Rf_protect, Rf_unprotect):
        self.libR = libR
        self.R_P_ACTIVE_BINDING = R_P_ACTIVE_BINDING
        self.R_P_METHOD_DISPATCH = R_P_METHOD_DISPATCH
        self.R_P_METHOD_LOOKUP = R_P_METHOD_LOOKUP
        self.R_P_SET_ACTIVE_BINDING = R_P_SET_ACTIVE_B
