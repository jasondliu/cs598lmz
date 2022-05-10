import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("hello")
    return None

winreg = ctypes.windll.LoadLibrary("advapi32.dll")
hkey = ctypes.c_void_p()
winreg.RegOpenKeyExA(0x80000002,"Software\\Microsof
