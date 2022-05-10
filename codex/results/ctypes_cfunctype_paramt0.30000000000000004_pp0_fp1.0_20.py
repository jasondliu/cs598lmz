import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def myfunc(a, b):
    return a + b

myfunc_c = FUNTYPE(myfunc)
print(myfunc_c(1, 2))

# 使用ctypes.windll.kernel32.GetCommandLineW()获取命令行参数
import ctypes
import sys

if sys.platform == 'win32':
    import ctypes.wintypes
    kernel32 = ctypes.windll.kernel32
    command_line_w = kernel32.GetCommandLineW()
    command_line_a = ctypes.wintypes.LPWSTR(command_line_w).encode('utf-8')
    print(command_line_a)

# 使用ctypes.windll.kernel32.GetCommandLineA()获取命令行参数
import ctypes
import sys

if sys.platform == 'win32':
    kernel32 =
