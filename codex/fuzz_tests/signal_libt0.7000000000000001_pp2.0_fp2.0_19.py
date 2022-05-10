import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def get_cursor_pos():
    return win32gui.GetCursorPos()

def get_pixel(x,y):
    return win32gui.GetPixel(win32gui.GetDC(0),x,y)

def clear_pixel(x,y):
    win32gui.SetPixel(win32gui.GetDC(0),x,y,0)

def clear_color(color):
    to_clear = []
    for x in range(0,1920):
        for y in range(0,1080):
            if get_pixel(x,y) == color:
                to
