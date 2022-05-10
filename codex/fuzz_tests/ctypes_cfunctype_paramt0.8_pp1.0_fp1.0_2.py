import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p,
                        ctypes.c_void_p,
                        ctypes.c_char_p,
                        ctypes.c_char_p,
                        ctypes.c_int,
                        ctypes.c_void_p)

class Callbacks(object):
    def __init__(self, _lib, _config_id):
        self._lib = _lib
        self._config_id = _config_id

    def vpn_read_callback(self):
        def callback(data, size, userdata):
            print("reading: %s %s %s" % (data, size, userdata))
            return 0
        return FUNTYPE(callback)

    def vpn_write_callback(self):
        def callback(data, size, userdata):
            print("writing: %s %s %s" % (data, size, userdata))
            return 0
        return FUNTYPE(callback)

    def on_connect_callback(self):
        def callback(connection_id, userdata):
            print("on_connect: %
