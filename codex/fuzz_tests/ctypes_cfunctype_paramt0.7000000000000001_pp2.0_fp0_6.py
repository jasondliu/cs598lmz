import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p)

try :
    lib = ctypes.CDLL("libpkcs11.so")
except :
    lib = ctypes.CDLL("libopencryptoki.so")

class CK_INFO(ctypes.Structure):
    _fields_ = [("cryptokiVersion", ctypes.c_ulong),
                ("manufacturerID", ctypes.create_string_buffer(32)),
                ("flags", ctypes.c_ulong),
                ("libraryDescription", ctypes.create_string_buffer(32)),
                ("libraryVersion", ctypes.c_ulong),]

class CK_SLOT_INFO(ctypes.Structure):
    _fields_ = [("slotDescription", ctypes.create_string_buffer(64)),
                ("manufacturerID", ctypes.create_string_buffer(32)),
                ("flags", ctypes.c_ulong),
                ("hardwareVersion", ctypes.c_ulong),
                ("firmwareVersion", ctypes.c_ulong),]

class CK_TOKEN
