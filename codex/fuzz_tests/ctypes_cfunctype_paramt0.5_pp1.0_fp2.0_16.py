import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(i):
    print("callback", i)
    return i

CALLBACK = FUNTYPE(callback)

lib = ctypes.CDLL("/home/michael/Projects/stdcall/build/libstdcall.so")
lib.callback_test(CALLBACK)

# I can't figure out how to create a ctypes callback from a simple function
# pointer.  So I've created a C++ wrapper class.  The class is defined in
# callback_wrapper.h.  The class is instantiated in callback_wrapper.cpp,
# and the function pointer is passed to the constructor.
#
# The callback_wrapper.cpp file is compiled into a shared object, and
# loaded into python using ctypes.
#
# The callback_wrapper.cpp file has a call to the function pointer.  The
# callback_wrapper.cpp file is compiled into a shared object, and loaded
# into python using ctypes.
#
# The callback_wrapper class has a call_callback method.  This method is
# called
