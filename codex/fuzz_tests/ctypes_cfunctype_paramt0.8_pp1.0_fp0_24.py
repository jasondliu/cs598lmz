import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_char_p, ctypes.c_char_p)

class python_helper(object):
    def __init__(self, helper_path, logger=default_logger_func):
        self.logger = logger
        self.dll = ctypes.cdll.LoadLibrary(helper_path)
        self.dll.main.argtypes = [ctypes.c_char_p, FUNTYPE]
        self.dll.main.restype = ctypes.c_void_p
        self.dll.free.argtypes = [ctypes.c_char_p]
        self.dll.free.restype = None
        self.dll.start_run.restype = None
        self.dll.set_script.argtypes = [ctypes.c_char_p]
        self.dll.set_script.restype = None

    def __del__(self):
        self.dll.main(None, None)

    def set_script(self, script):
        script = os.path.abspath(script)
        self.
