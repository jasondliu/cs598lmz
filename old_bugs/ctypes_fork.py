from os import fork, waitpid
import ctypes

def func():
    pass

cfunc = ctypes.CFUNCTYPE(None)(func)

pid = fork()
if pid:
    waitpid(pid, 0)
