import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

signal.signal(signal.SIGALRM, fun)
signal.alarm(3)

while True:
    pass
