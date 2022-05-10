import ctypes
ctypes.windll.shell32.IsUserAnAdmin()

if is_admin:
    import win32event, win32api, winerror
    from _winreg import *

    # grab the handle to the main window
    hWnd = win32console.GetConsoleWindow()

    # hide the window
    win32gui.ShowWindow(hWnd,0)

    # if the window was already hidden,
    # then Python (win32gui) will NOT
    # return a handle to the window;
    # so if hWnd is still equal to
    # its default value then the window
    # must have already been hidden
    # so we can exit the script NOW!
    if hWnd == 0:
        exit(0)

    # create and register the window class
    window_class=win32gui.WNDCLASS()
    hinst=window_class.hInstance=win32api.GetModuleHandle(None)
    window_class.lpszClassName="PythonTaskbarDemo"
    window_class.style=win32con.CS_VREDRAW | win32con
