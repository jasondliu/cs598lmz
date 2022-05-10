import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

assert type(fun) is FUNTYPE
fun()

# This is the code that doesn't work...
msvcrt = ctypes.windll.msvcrt
def_init = msvcrt.__init__

@FUNTYPE
def my_init(self):
    # Call the original initialization method.
    def_init(self)
    # Save a method handle to the original error routine.
    self._err_fn = msvcrt.__stderr__
    # Override the error routine.
    msvcrt.__stderr__ = self._err_fn

# Install our initialization routine.
msvcrt.__init__ = my_init

# Attempt to reproduce the error.
def init():
    try:
        return -1
    except Exception as exc:
        raise ctypes.WinError(ctypes.get_last_error())

init()
</code>

