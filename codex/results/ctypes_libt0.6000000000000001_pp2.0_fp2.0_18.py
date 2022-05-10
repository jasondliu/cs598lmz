import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

# Import ctypes.wintypes
import ctypes.wintypes

# Structure variable
class GUID(ctypes.Structure):
    _fields_ = [
        ("Data1", ctypes.wintypes.DWORD),
        ("Data2", ctypes.wintypes.WORD),
        ("Data3", ctypes.wintypes.WORD),
        ("Data4", ctypes.c_byte * 8)
    ]

# Create GUID
guid = GUID(0x30630201, 0xaa6b, 0x44e7, (ctypes.c_byte*8)(0x82, 0x06, 0xec, 0x82, 0x27, 0x1d, 0x4f, 0x53))

# Call API
ctypes.windll.ole32.CoCreateGuid(ctypes.byref(guid))

# Print GUID
print(guid.Data1)
print(guid.Data
