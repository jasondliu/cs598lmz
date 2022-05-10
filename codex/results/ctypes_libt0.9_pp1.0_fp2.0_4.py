import ctypes
ctypes.windll.user32.SetProcessDPIAware()
windll.user32.EnumWindows.restype=ctypes.c_bool
windll.user32.EnumWindows.argtypes=(ctypes.c_void_p,ctypes.c_int32)
window_h=[]
def wind_enum(h,l):
    window_h.append(h)
    return True

windll.user32.EnumWindows(wind_enum,0)
print(window_h)
for i in window_h:
    # GetWindowRect(i, lpRect)
    # print("width:%d,height:%d" %(lpRect.right-lpRect.left,lpRect.bottom-lpRect.top))
    # print("X:%d,Y:%d" % (lpRect.left,lpRect.top))
    # GetWindowText(i, lpText, lpMaxTextLength)
    # GetWindowTextLength(i)
    # print(lpText.value)
    # print(lpTextLength)
    b=
