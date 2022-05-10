import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))

class C(object):
    def __init__(self, callback):
        self.callback = callback

    @property
    def callback_func(self):
        # Get the address of the Python callback
        cb = self.callback.__func__
        cb_ptr = ctypes.cast(ctypes.pointer(cb), ctypes.c_void_p).value

        # Convert it to a function pointer
        FUNC = FUNTYPE(cb_ptr)
        return FUNC

    def trigger(self, n):
        # Call the callback from C code
        result = self.callback_func(n)
        return result


c = C(lambda n: n.contents.value * 2)
n = ctypes.c_int(2)
print(c.trigger(n))
# 4
</code>

