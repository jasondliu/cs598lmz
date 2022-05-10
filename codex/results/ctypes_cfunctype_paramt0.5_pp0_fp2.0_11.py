import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_char_p)

def callback(arg):
    print('callback:', arg.decode('utf-8'))

CALLBACK = FUNTYPE(callback)

dll = ctypes.cdll.LoadLibrary('libfoo.so')
dll.foo(CALLBACK)
</code>

