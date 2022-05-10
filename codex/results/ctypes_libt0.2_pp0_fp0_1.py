import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

# import win32api
# win32api.MessageBox(0, 'Python 你好！', '你好', win32con.MB_OK)

# import win32gui
# win32gui.MessageBox(0, 'Python 你好！', '你好', win32con.MB_OK)

# import win32ui
# win32ui.MessageBox('Python 你好！', '你好', win32con.MB_OK)

# import win32con
# import win32gui
#
# def callback(hwnd, extra):
#     rect = win32gui.GetWindowRect(hwnd)
#     x = rect[0]
#     y = rect[1]
#     w = rect[2] - x
#     h = rect[3] - y
#     print("Window %s:" % win32gui.GetWindowText(hwnd))
#     print("
