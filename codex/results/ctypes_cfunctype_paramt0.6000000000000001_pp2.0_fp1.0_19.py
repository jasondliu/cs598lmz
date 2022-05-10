import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

_testfunc = ctypes.pythonapi.PyThreadState_SetAsyncExc
_testfunc.argtypes = [ctypes.c_long, FUNTYPE]

def interrupt_thread(thread_id):
    found = False
    for tid, tobj in threading._active.items():
        if tid == thread_id:
            found = True
            break

    if not found:
        raise ValueError("Invalid thread id")

    res = _testfunc(tid, None)
    if res == 0:
        raise ValueError("Invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        _testfunc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

def close_thread(thread):
    interrupt_thread(thread.ident)
    thread.join()

def set_interrupt(thread):
    _testfunc(thread.ident, lambda: None)
</
