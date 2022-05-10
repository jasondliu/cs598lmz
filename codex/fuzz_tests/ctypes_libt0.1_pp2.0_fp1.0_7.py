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
# def win_msg(hwnd, msg, wp, lp):
#     if msg == win32con.WM_DESTROY:
#         win32gui.PostQuitMessage(0)
#     else:
#         return win32gui.DefWindowProc(hwnd, msg, wp, lp)
#
# win32gui.MessageBox(0, 'Python
