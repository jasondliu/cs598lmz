import ctypes
# Test ctypes.CFUNCTYPE()
Address = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)

class Request(ctypes.Structure):
  _fields_ = [('userdata', ctypes.c_void_p),
              ('notifyaddr', Address)]

