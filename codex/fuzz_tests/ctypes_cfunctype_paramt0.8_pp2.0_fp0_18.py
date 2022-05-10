import ctypes
FUNTYPE = ctypes.CFUNCTYPE( ctypes.c_int
                         , ctypes.c_int, ctypes.c_int, ctypes.c_int
                         , ctypes.POINTER(ctypes.c_byte)
                         , ctypes.POINTER(ctypes.c_int)
                         , ctypes.POINTER(ctypes.c_int)
                         , ctypes.POINTER(ctypes.c_int)
                         )

class Plugin(object):
    def __init__(self):
        self.module_name = None
        self.module = None
        self.is_loaded = False
        self.plugin_id = None
        self.plugin_info = None
        self.plugin_handle = None
        self.plugin_api = {}
        self.plugin_init = None
        self.plugin_done = None
        self.context = None
        self.api = None
        self.name = None
        self.author = None
        self.version = None
        self.license = None
        self.config_type = None
        self.enable_configuration = None
        self
