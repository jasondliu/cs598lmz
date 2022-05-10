import ctypes
FUNTYPE = ctypes.CFUNCTYPE( None, ctypes.c_int, ctypes.c_int,
                           ctypes.c_int, ctypes.c_int, ctypes.c_int )

def callback( hwnd, msg, id1, id2, time ):
    """
    hwnd: the window handle
    msg: the message ID
    id1: message parameter
    id2: message parameter
    time: the time that the message was posted
    """
    print "callback", hwnd, msg, id1, id2, time
    return True
CB_FUNCTYPE = FUNTYPE( callback )

win32lib.SetWindowsHookEx( win32con.WH_KEYBOARD, CB_FUNCTYPE, 0, win32lib.GetCurrentThreadId() )

win32lib.PostThreadMessage( win32lib.GetCurrentThreadId(), win32con.WM_KEYDOWN, win32con.VK_TAB, 1 )

win32lib.UnhookWindowsHookEx( CB_FUNCTYPE )
</code>
When I run this program, I get
