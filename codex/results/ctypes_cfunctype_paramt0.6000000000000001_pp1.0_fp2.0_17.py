import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

class HID_DEVICE_ATTRIBUTES(ctypes.Structure):
    _fields_ = [("Size", ctypes.c_ulong),
                ("VendorID", ctypes.c_ushort),
                ("ProductID", ctypes.c_ushort),
                ("VersionNumber", ctypes.c_ushort)]

class HidD_GetHidGuid(ctypes.Structure):
    pass

HidD_GetHidGuidProto = FUNTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
HidD_GetHidGuidParams = (1, "HidGuid", 0),
HidD_GetHidGuid = HidD_GetHidGuidProto(("HidD_GetHidGuid", hid), HidD_GetHidGuidParams)

HidD_GetHidGuid.restype = ctypes.c_int
HidD_GetHidGuid.argtypes = [ctypes
