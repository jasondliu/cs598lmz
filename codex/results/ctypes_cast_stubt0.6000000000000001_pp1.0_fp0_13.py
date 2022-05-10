import ctypes
ctypes.cast(addr, ctypes.py_object).value

#%%
# ctypes 另外一个强大的特性就是可以通过它来调用 C 函数
# C 语言的函数库头文件，详细请参见：https://en.wikibooks.org/wiki/C_Programming/C_Reference/stdlib.h
#! /usr/bin/env python
# -*- coding:utf-8 -*-

from ctypes import *
import os

# 给 C 的一个函数传递一个 Python 字符串
# 先声明一个 C 的字符串函数
# C 的函数
libc = CDLL('./libc.so.6')
# 调用 C 的
