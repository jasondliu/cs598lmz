import ctypes
# Test ctypes.CFUNCTYPE(None)

def callback():
    print("callback")

CALLBACK = ctypes.CFUNCTYPE(None)

@CALLBACK
def callback():
    print("callback")

#@CALLBACK
#def callback():
#    print("callback")

#@CALLBACK
#def callback():
#    print("callback")

#@CALLBACK
#def callback():
#    print("callback")

#@CALLBACK
#def callback():
#    print("callback")

#@CALLBACK
#def callback():
#    print("callback")

#@CALLBACK
#def callback():
#    print("callback")

#@CALLBACK
#def callback():
#    print("callback")

#@CALLBACK
#def callback():
#    print("callback")

#@CALLBACK
#def callback():
#    print("callback")

#@CALLBACK
#def callback():
#    print("callback")

#@CALLBACK
#def callback():
#    print("callback
