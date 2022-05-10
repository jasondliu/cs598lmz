import ctypes
# Test ctypes.CFUNCTYPE(None)

def callback():
    print("callback")

CALLBACK = ctypes.CFUNCTYPE(None)

@CALLBACK
def callback():
    print("callback")

#@CALLBACK(None)
#def callback():
#    print("callback")

#@CALLBACK(ctypes.c_int)
#def callback(arg):
#    print("callback", arg)

#@CALLBACK(ctypes.c_int, ctypes.c_int)
#def callback(arg1, arg2):
#    print("callback", arg1, arg2)

#@CALLBACK(ctypes.c_int, ctypes.c_int, ctypes.c_int)
#def callback(arg1, arg2, arg3):
#    print("callback", arg1, arg2, arg3)

#@CALLBACK(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
#def callback(arg1, arg2, arg3,
