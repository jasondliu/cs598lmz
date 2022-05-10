import ctypes
# Test ctypes.CFUNCTYPE()
def f():
    return 1

cf = ctypes.CFUNCTYPE(ctypes.c_int, argtypes=[])(f)

print cf()
print cf()

# Test ctypes.WINFUNCTYPE()
#import ctypes.wintypes
#
#def f():
#    return 1
#
#wf = ctypes.WINFUNCTYPE(ctypes.c_int, argtypes=[])(f)
#print wf()
#print wf()
#
#import ctypes.wintypes
#
#WM_KEYDOWN = 0x0100
#WM_KEYUP = 0x0101
#WM_CHAR = 0x0102
#WM_DEADCHAR = 0x0103
#WM_SYSKEYDOWN = 0x0104
#WM_SYSKEYUP = 0x0105
#WM_SYSCHAR = 0x0106
#WM_SYSDEADCHAR = 0x0107
#
#def lowlevel_handler(nCode, wParam, lParam):
#    print 'lowlevel
