import ctypes
FUNTYPE = ctypes.CFUNCTYPE( ctypes.c_int )
# Use the above type to cast this function to the required prototype.
# This variable can now be used as argument to libpyspotify.
sp_session_set_connection_type = FUNTYPE( _sp_session_set_connection_type )

def _sp_session_process_events(self, timeout):
    """
    C wrapper for:

    int sp_session_process_events(sp_session *session, int timeout)

    """
    return sp_session._sp_session_process_events(self, timeout)
# First argument is always self.
# We have to cast this function to the required type.
# <ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_int)> ensures that the first
# argument is the pointer to the Python object, and the second is an int.
FUNTYPE = ctypes.CFUNCTYPE( ctypes.c_int, ctypes.c_void_p, ctypes.c_int )
# Use the above type to cast this function to the required prototype
