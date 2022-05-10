import ctypes
ctypes.windll.shell32.IsUserAnAdmin()

# 获取进程的权限
import os
import ctypes
import win32api
import win32process
import win32security

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin(cmdLine=None, wait=True):
    if os.name != 'nt':
        raise RuntimeError("This function is only implemented on Windows.")

    if cmdLine is None:
        cmdLine = '"{}"'.format(sys.executable)
    elif isinstance(cmdLine, (list, tuple)):
        cmdLine = '"{}" "{}"'.format(sys.executable, '" "'.join(cmdLine))
    elif not isinstance(cmdLine, str):
        raise ValueError("cmdLine is not a string.")

    # 检查当前进程是否具有管理
