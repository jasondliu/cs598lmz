import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None
fun()
</code>
This fails for me with
<code>Fatal Python error: PyEval_EvalFrameEx: NULL tstate
</code>

Update: The problem happens when using the C API from another thread. In this case the GIL (global interpreter lock) is not held and thus the interpreter gets into an inconsistent state.
I found that the following works:
<code>from ctypes import c_long, c_char_p, pythonapi, py_object
from ctypes import CFUNCTYPE, POINTER
from threading import Thread
import sys

def fun():
    print('hello world')

def do_thread():
    # create a new thread and switch to it
    tid = c_long(-1)
    if pythonapi.PyThreadState_New(c_long(pythonapi.PyThreadState_Get())) &lt; 0:
        raise RuntimeError('cannot switch to new thread')
    pythonapi.PyEval_InitThreads()
    pythonapi.PyEval_ReleaseThread(pythonapi.PyThreadState_Get())
   
