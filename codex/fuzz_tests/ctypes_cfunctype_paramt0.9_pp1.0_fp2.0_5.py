import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)

# We use this global method to trap objects that may cause a
# segfault.
_trapped_object = None  # pylint: disable=invalid-name

import os
lib = ctypes.cdll.LoadLibrary(os.path.join(os.path.dirname(__file__), 'cudamisc.so'))
def trap_errors(func):
    """
    Wrap a function to trap segfaults.
    """
    def inner(self, *args):
        global _trapped_object
        self_ref = weakref.ref(self)
        def error_handler(string): # pylint: disable=unused-argument
            _trapped_object = str(self_ref())
            return 1

        error_handler_func = FUNTYPE(error_handler)
        error_handler_id = lib.trap_cuda_errors(error_handler_func)

        try:
            return func(self, *args)
        except:  # pyl
