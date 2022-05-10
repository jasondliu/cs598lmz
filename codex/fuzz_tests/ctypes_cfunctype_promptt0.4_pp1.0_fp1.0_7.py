import ctypes
# Test ctypes.CFUNCTYPE
def test_CFUNCTYPE():
    # ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
    # restype: 被调用函数返回值类型
    # argtypes: 被调用函数参数类型
    # use_errno: 是否使用errno
    # use_last_error: 是否使用GetLastError()

    # 调用win32的MessageBoxA函数
    # MessageBoxA(hwnd, text, caption, type)
    # hwnd: 父窗口句柄
    # text: 消息文本
    # caption: 消息标题
    # type: 消息类型

    # 定义MessageBoxA
