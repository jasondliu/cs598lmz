import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('mycompany.myproduct.subproduct.version')

#改变窗口图标
from ctypes import windll

main_hwnd = windll.user32.GetForegroundWindow()
icon = windll.user32.LoadIconW(0, "E:\Python\Project\PyQt5\Test\logo.ico")
windll.user32.SendMessageW(main_hwnd, 0x80, 1, icon)

#改变窗口标题
from ctypes import windll

main_hwnd = windll.user32.GetForegroundWindow()
windll.user32.SetWindowTextW(main_hwnd, "标题")

#获取窗口句柄
from ctypes import windll

main_hwnd = windll.user32.GetForegroundWindow()
print(main_hwnd)

#设置
