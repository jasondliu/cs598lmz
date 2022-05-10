import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int, ctypes.c_int,
                           ctypes.POINTER(ctypes.c_double))
CALLBACK1 = FUNTYPE(lambda c, d, e: e[0] + e[1])
CALLBACK2 = FUNTYPE(lambda c, d, e: e[0] * e[1])

DEFAULT_KWARGS_1 = {'param_types': [int, int, [float, 2, 'a']],
                    'param_names': ['c', 'd', 'e'],
                    'return': double}
DEFAULT_KWARGS_2 = {'param_types': [[float, 2, 'a']],
                    'param_names': ['e'],
                    'return': double}

import functools

def get_callback_function(func, kwargs, reuse=False):
    """Get the correct callback function from the given function and keyword
    arguments.

    Parameters
    ----------
    func : callable
        The function that should be called for the callback.

   
