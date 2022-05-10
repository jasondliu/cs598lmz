import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

# These are "private" functions and should not be called from outside this
# module.
_callback_map = {}
_callback_map_lock = threading.Lock()
_callback_id_map = {}
_callback_id_lock = threading.Lock()
_callback_id_gen = 0

def _cleanup_callback(callback_id):
    global _callback_map
    global _callback_id_map
    global _callback_id_gen

    _callback_map_lock.acquire()
    try:
        del _callback_map[callback_id]
    finally:
        _callback_map_lock.release()

    _callback_id_lock.acquire()
    try:
        del _callback_id_map[callback_id]
    finally:
        _callback_id_lock.release()

    _callback_id_gen -= 1

def _add_callback(callback):
    global _callback_map
    global _callback_id_map
    global _callback_id_gen

    callback_id = _callback_id
