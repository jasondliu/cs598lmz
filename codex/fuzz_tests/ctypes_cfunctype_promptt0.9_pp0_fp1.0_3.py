import ctypes
# Test ctypes.CFUNCTYPE
from ctypes import *
import datetime
import time


#计数器
count = 0

#存储数据的列表
data_list=[[],[],[]]

def create_string_buffer(init, size=None):
    if size is None:
        size = len(init)
    return (ctypes.c_char * size).from_buffer_copy(init)

def format_float(n):
    if type(n) != str:
        n = '%.4f' % n
    return create_string_buffer(n.encode('ascii'), 16)

def format_int(n):
    if type(n) != str:
        n = '%d' % n
    return create_string_buffer(n.encode('ascii'), 16)


########################################################################
#价格回调函数
#当收到行情时，会自动触发
