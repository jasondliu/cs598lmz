import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

def call_on_main_thread(func):
    """
    Calls a function on the main thread.
    """
    is_main_thread = (threading.current_thread() == threading.main_thread())
    if is_main_thread:
        func()
    else:
        cefpython.PostTask(cefpython.TID_UI, FUNTYPE(func))
</code>

