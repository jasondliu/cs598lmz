import ctypes
import ctypes.util
import threading
import sqlite3

_lg = ctypes.cdll.LoadLibrary(ctypes.util.find_library("lg"))
_lg.lg_context_new.restype = ctypes.POINTER(object)
_lg.lg_context_new.argtypes = [ctypes.c_char_p]
_lg.lg_context_free.argtypes = [ctypes.POINTER(object)]
_lg.lg_context_run.argtypes = [ctypes.POINTER(object)]
_lg.lg_context_wait.argtypes = [ctypes.POINTER(object)]
_lg.lg_context_run_script.argtypes = [ctypes.POINTER(object), ctypes.c_char_p]
_lg.lg_context_run_script.restype = ctypes.c_int
_lg.lg_context_create_task_from_data.argtypes = [ctypes.POINTER(object), ctypes.c_char_p]
_lg.lg_context_create
