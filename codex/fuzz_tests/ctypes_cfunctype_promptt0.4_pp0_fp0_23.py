import ctypes
# Test ctypes.CFUNCTYPE()
def func(a, b):
    return a + b

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

cmp_func = CMPFUNC(func)
print cmp_func(1, 2)

# Test ctypes.WINFUNCTYPE()
WM_USER = 1024

WNDPROC = ctypes.WINFUNCTYPE(ctypes.c_long, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(hwnd, msg, wparam, lparam):
    if msg == WM_USER:
        print "Hello, world!"
        return 0
    else:
        return ctypes.windll.user32.DefWindowProcA(hwnd, msg, wparam, lparam)

proc = WNDPROC(my_callback)

ctypes.windll.user32.PostMessageA(0, WM_USER, 0, 0
