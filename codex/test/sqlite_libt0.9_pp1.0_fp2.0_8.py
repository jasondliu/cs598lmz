import ctypes
import ctypes.util
import threading
import sqlite3


connection = sqlite3.connect(sys.path[0] + "\database.db")
cursor = connection.cursor()


def login():
    if sys.platform == 'win32':
        libc = ctypes.windll.LoadLibrary('libasound-2.dll')
    elif sys.platform == 'darwin':
        libc = ctypes.cdll.LoadLibrary('libasound.dylib')
    else:
        libc = ctypes.cdll.LoadLibrary(ctypes.util.find_library('asound'))
    libc.snd_lib_error_set_handler(0)
    global devids

    device_count = libc.snd_device_name_hint(-1, b'pcm', ctypes.pointer(ctypes.c_int()))

    if device_count >= 0:
        devidslist = ctypes.pointer(ctypes.c_char_p())
        libc.snd_device_name_hint(-1, b'pcm', ctypes.pointer(devidslist))

