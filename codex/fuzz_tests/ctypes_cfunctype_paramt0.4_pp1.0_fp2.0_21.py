import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

def _as_parameter_ (self):
    return self._as_parameter_

def _set_fun_type_ (self, funtype):
    self._funtype_ = funtype

def _get_fun_type_ (self):
    return self._funtype_

def _set_callback_ (self, callback):
    self._callback_ = callback

def _get_callback_ (self):
    return self._callback_

def _set_userdata_ (self, userdata):
    self._userdata_ = userdata

def _get_userdata_ (self):
    return self._userdata_

def _set_errcheck_ (self, errcheck):
    self._errcheck_ = errcheck

def _get_errcheck_ (self):
    return self._errcheck_

def _set_restype_ (self, restype):
    self._restype_ = restype

def _get_restype_ (self):
    return self._restype_

def _set_argtypes_ (
