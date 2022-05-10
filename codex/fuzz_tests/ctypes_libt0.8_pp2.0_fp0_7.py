import ctypes
ctypes.windll.user32.LoadImageW.restype = ctypes.wintypes._HANDLE
ctypes.windll.user32.LoadImageW.argtypes = [ ctypes.wintypes.HINSTANCE, ctypes.wintypes.LPCWSTR, \
                                             ctypes.wintypes.UINT, ctypes.c_int, ctypes.c_int, \
                                             ctypes.wintypes.UINT ]

class Bitmap(object):
    __slots__ = ( '__path', '__data' )
    def __new__(cls, path=None, data=None, width=None, height=None, depth=None):
        if path:
            raw = ctypes.windll.user32.LoadImageW(0, path, 1, width or 0, height or 0, depth or 0x10)
            if raw:
                obj = object.__new__(cls)
                obj.path = path
                obj.data = raw
                return obj

    def __repr__(self):
        return '
