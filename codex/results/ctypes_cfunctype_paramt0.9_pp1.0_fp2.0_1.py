import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

class Event():
    def __init__(self, function):
        self.fid = FUNTYPE(function)

    def __call__(self, *args, **kwargs):
        self.fid()
