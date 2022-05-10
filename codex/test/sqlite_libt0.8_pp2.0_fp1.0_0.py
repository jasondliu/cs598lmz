import ctypes
import ctypes.util
import threading
import sqlite3
import random
import pprint
import sys
import time
import demjson
import requests

# 判断PYTHON版本
if sys.version_info[0] == 3:
    # python3
    from tkinter import *
    from tkinter.scrolledtext import ScrolledText
else:
    # python2
    from Tkinter import *
    from ScrolledText import ScrolledText

print("*" * 10 + "  前置安装  " + "*" * 10)
print("1.python3")
print("2.pypiwin32")
print("3.requests")
print("4.demjson")
print("5.pypiwin32、demjson、requests使用pip安装")
print("\n")

root = Tk()
root.title("按键摇动")
root.geometry("640x480")


class MainWindow:

    def __init__(self):
        self.lblAbsolute = Label
