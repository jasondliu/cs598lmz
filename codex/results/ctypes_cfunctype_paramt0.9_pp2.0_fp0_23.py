import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)
def get_EINTR_callable():
    func = FUNTYPE(lambda x: x == 4)
    def func_wrapper():
        if func():
            raise IOError(errno.EINTR, "Interrupted system call")
    return func_wrapper

EINTR_callable = get_EINTR_callable()
</code>

