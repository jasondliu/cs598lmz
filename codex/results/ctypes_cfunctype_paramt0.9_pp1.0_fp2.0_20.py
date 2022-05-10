import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Emulated implementation of the UNO struct
from ctypes import cast, c_char_p, c_void_p
class UNOStruct(ctypes.Structure):
    _fields_ = [
        ('XInterface', c_void_p),
        ('acquire', FUNTYPE(None)),
        ('release', FUNTYPE(None)),
        ('queryInterface', FUNTYPE(None)),
    ]
    def __init__(self, **kwargs):
        lib, interface, acquire, release, acquireFunc, releaseFunc, interfaceFunc = kwargs.pop('externals')
        self.acquire = acquire
        self.release = release
        self._acquireFunc = acquireFunc
        self._releaseFunc = releaseFunc
        self._interfaceFunc = interfaceFunc
        self._lib = lib
        self._interface = interface
        self._interfaceName = ctypes.create_string_buffer(interface.encode('utf-8'))
        if kw
