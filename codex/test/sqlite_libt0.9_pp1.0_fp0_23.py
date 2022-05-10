import ctypes
import ctypes.util
import threading
import sqlite3

class udev (object):
  """
  Some low-level methods to interface with libudev.
  """

  def __init__ (self):
    self._libudev = ctypes.cdll.LoadLibrary (ctypes.util.find_library ('udev'))
    self._libudev.udev_list_entry_get_next.argtypes = [ctypes.c_void_p]
    self._libudev.udev_list_entry_get_name.argtypes = [ctypes.c_void_p]
    self._libudev.udev_enumerate_add_match_subsystem.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p]
    self._libudev.udev_enumerate_scan_devices.argtypes = [
        ctypes.c_void_p]
    self._libudev.udev_enumerate_get_list_entry.argtypes = [
        ctypes.c_void_p]
    self._libud
