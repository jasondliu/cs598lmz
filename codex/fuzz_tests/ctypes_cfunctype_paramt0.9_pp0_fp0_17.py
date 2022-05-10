import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int)

##
## 定義回傳函式
## 說明：可在執行底下命令生成引入的C函式定義：
## （使用python IDLE）
#    >>> from ctypes import *
#    >>> windll.kernel32.GetStdHandle.argtypes = [c_int]
#    >>> windll.kernel32.GetStdHandle.restype = c_int
#    >>> windll.kernel32.GetStdHandle.__doc__
#    u'GSH_W'        


## 定義取得標準輸入輸出設備集合
windll.kernel32.GetStdHandle.argtypes = [ctypes.c_ulong]
windll.kernel32.GetStdHandle.restype = c
