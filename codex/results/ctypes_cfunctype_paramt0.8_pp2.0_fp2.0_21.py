import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_char_p)


def self_check(msg):
    print(msg.decode('utf-8'))
lib = ctypes.CDLL('./libpython.so', ctypes.RTLD_GLOBAL)
func = FUNTYPE(lib.self_check)
func('this is from python'.encode('utf-8'))
#func('dasad'.encode('utf-8'))
