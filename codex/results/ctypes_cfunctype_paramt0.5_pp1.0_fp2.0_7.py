import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)

def _signal_handler(signum, frame):
    raise KeyboardInterrupt

def _set_signal_handlers():
    signal.signal(signal.SIGINT, _signal_handler)
    signal.signal(signal.SIGTERM, _signal_handler)

def _unset_signal_handlers():
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    signal.signal(signal.SIGTERM, signal.SIG_DFL)

def _set_signal_handler_c(handler):
    libc = ctypes.CDLL(None)
    c_handler = FUNTYPE(handler)
    libc.signal(signal.SIGINT, c_handler)
    libc.signal(signal.SIGTERM, c_handler)

def _unset_signal_handler_c():
    libc = ctypes.CDLL(None)
    c
