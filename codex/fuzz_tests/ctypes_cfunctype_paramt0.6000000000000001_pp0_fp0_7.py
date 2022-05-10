import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)

def get_event_loop():
    return libev.ev_default_loop()

def run(loop, flags = 0):
    libev.ev_run(loop, flags)

def run_once(loop, flags = 0):
    libev.ev_run(loop, flags | libev.EVRUN_ONCE)

def run_nowait(loop, flags = 0):
    libev.ev_run(loop, flags | libev.EVRUN_NOWAIT)

def break_loop(loop, how = libev.EVBREAK_ALL):
    libev.ev_break(loop, how)

def break_loop_return_code(loop):
    return libev.ev_break_loop_return_code(loop)

def now(loop):
    return libev.ev_now(loop)

def update_now(loop):
    libev.ev_now_update(loop)

def backend_fd(loop):
    return lib
