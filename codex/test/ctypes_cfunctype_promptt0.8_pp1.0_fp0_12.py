import ctypes
# Test ctypes.CFUNCTYPE()
import datetime
import os
import sys
import time

# 系统是64位
# print(sys.maxsize > 2 ** 32)

# 库路径问题
# print(os.getcwd())  # 获取当前目录
# print(os.path.dirname(__file__))  # 获取文件所在目录，如果是相对路径，会是模块所在目录，如果是绝对路径，就是文件的绝对路径
# print(os.path.abspath(__file__))  # 获取文件的绝对路径
# print(os.path.realpath(__file__))  # 获取文
