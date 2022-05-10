import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,
                           ctypes.POINTER(ctypes.c_char_p),
                           ctypes.POINTER(ctypes.c_char_p))

def load(filename):
    """Load a trained model from a file, and create a predictor.

    Parameters
    ----------
    filename : str
        Path to the model file.

    Returns
    -------
    predictor : Predictor
        The predictor that runs the model.
    """
    _check_call(_LIB.XGBoosterCreate(ctypes.c_char_p(filename.encode('utf-8')),
                                     ctypes.byref(ctypes.c_ulong())))
    handle = ctypes.c_void_p()
    _check_call(_LIB.XGBoosterLoadModel(ctypes.byref(handle),
                                        ctypes.c_char_p(filename.encode('utf-8'))))
    return Predictor(handle)

def train(params, dtrain, num_boost_round=10, evals=(), obj=None,
