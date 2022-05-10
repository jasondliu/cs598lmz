import ctypes
# Test ctypes.CFUNCTYPE
prototype = CFUNCTYPE(c_int, c_int, c_int)
# Test the rest of the functions if running in Python 2
if sys.version_info[0] < 3:
    c_int_p = POINTER(c_int)
    prototype = CFUNCTYPE(c_int, c_int_p, c_int_p)
    PyCFuncPtr = prototype
    prototype = CFUNCTYPE(c_int, c_int, c_int, c_int)
    PyCObject_to_handler = prototype

# Register a series of callbacks
class Callbacks(object):

    def __init__(self):
        self.callbacks = {}

    def register(self, callback, data):
        id = len(self.callbacks)
        self.callbacks[id] = callback, data
        return id

    def fire(self, id):
        return self.callbacks.get(id, (None,None))[0](
            self.callbacks.get(id, (None,None))[1])


