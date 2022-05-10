import ctypes
# Test ctypes.CFUNCTYPE
#
# The ctypes.CFUNCTYPE factory function is used to create C function
# pointer types.
#
# The first argument is the return type, followed by the argument types.
#
# The function pointer type can be used to create callbacks, or to access
# DLL exported functions.

# The following example creates a callback function:

import sys
if sys.platform == "win32":
    STD_OUTPUT_HANDLE = -11
    std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

# Windows defines the following callback function type:
# WINAPI
# VOID
# CALLBACK
# TimerProc(
#     HWND hwnd,
#     UINT uMsg,
#     UINT_PTR idEvent,
#     DWORD dwTime);

def hello_world(hwnd, msg, id, time):
    print "Hello, World!"

TimerProc = ctypes.CFUNCTYPE(None, ctypes.c_int,
