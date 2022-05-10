import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def _make_callback(callback):
    cb = FUNTYPE(callback)
    return cb

def _make_callback_with_user_data(callback):
    cb = FUNTYPE(callback)
    return cb

def _make_callback_with_user_data_and_extra_args(callback):
    cb = FUNTYPE(callback)
    return cb

def _make_callback_with_extra_args(callback):
    cb = FUNTYPE(callback)
    return cb

def _make_callback_with_return(callback):
    cb = FUNTYPE(callback)
    return cb

def _make_callback_with_user_data_and_return(callback):
    cb = FUNTYPE(callback)
    return cb

def _make_callback_with_user_data_and_extra_args_and_return(callback):
    cb = FUNTYPE(callback)
    return cb

def _make_callback_with_extra_
