import ctypes

class S(ctypes.Structure):
    x = ctypes.create_string_buffer(b"hello")
