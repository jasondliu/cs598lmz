import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_char_p, ctypes.c_char_p)

def mycallback(arg):
    print('\n%s' % arg.decode('utf-8'))
    return b'\0'

CDLL_NAME = "./libchat.so"
cdll.LoadLibrary(CDLL_NAME)
dll = CDLL(CDLL_NAME)
dll.RegisterCallback(FUNTYPE(mycallback))

#dll.echo.restype = ctypes.c_char_p
#dll.echo.argtypes = [ctypes.c_char_p]

dll.do_connect.restype = ctypes.c_char_p
dll.do_connect.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]

dll.do_disconnect.restype = ctypes.c_char_p
#dll.do_disconnect.argtypes = []

dll.do_message.restype = ctypes.c_char_p
dll.do_message
