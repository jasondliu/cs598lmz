import ctypes
import ctypes.util
import threading
import sqlite3 as sqlite

class _BinarySearchTreeNode(ctypes.Structure):
  _fields_ = [('left', ctypes.c_void_p), ('right', ctypes.c_void_p), ('parent', ctypes.c_void_p), ('value', ctypes.c_long), ('key', ctypes.c_char_p)]

class BinarySearchTree(threading.Thread):
  _lib = ctypes.CDLL(ctypes.util.find_library('libbst'))
  _lib.bst_create.argtypes = []
  _lib.bst_create.restype = ctypes.c_void_p
  _lib.bst_destroy.argtypes = [ctypes.c_void_p]
  _lib.bst_destroy.restype = None
  _lib.bst_insert.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_long]
  _lib.bst_insert.restype = ctypes.c_long
  _lib
