import ctypes
import ctypes.util
import threading
import sqlite3


# Import moudle for fcitx input library function
fcitx = ctypes.cdll.LoadLibrary(ctypes.util.find_library('fcitx-config'))

fcitx.fcitx_config_new.restype = ctypes.c_void_p
fcitx.fcitx_config_new.argtypes = [ctypes.c_char_p, ctypes.c_int]
fcitx.fcitx_config_sync.restype = ctypes.c_int
fcitx.fcitx_config_sync.argtypes = [ctypes.c_void_p]
fcitx.fcitx_config_save.restype = ctypes.c_int
fcitx.fcitx_config_save.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
fcitx.fcitx_config_navigate.restype = ctypes.c_void_p
