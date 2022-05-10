import ctypes
ctypes.cast(1, ctypes.py_object)

# pylint: disable=E1101
_libraries['libpulse.so.0'] = CDLL('libpulse.so.0')
_libraries['libpulse.so.0'].pa_context_connect.restype = c_int
_libraries['libpulse.so.0'].pa_context_connect.argtypes = [POINTER(pa_context), c_char_p, pa_context_flags_t, POINTER(pa_spawn_api)]
_libraries['libpulse.so.0'].pa_context_disconnect.restype = None
_libraries['libpulse.so.0'].pa_context_disconnect.argtypes = [POINTER(pa_context)]
_libraries['libpulse.so.0'].pa_context_drain.restype = c_int
_libraries['libpulse.so.0'].pa_context_drain.argtypes = [POINTER(pa_context), pa_context_notify_cb_t, POINTER
