import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(): return "Hello, World"

#ctypes.windll.kernel32.MessageBoxA(0, fun(), "first ctypes.py_object", 0)
#ctypes.windll.kernel32.MessageBoxA(0, fun().value, "for ctypes.py_object.value", 0)

#Quit(0)
