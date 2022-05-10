import ctypes
ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

import win32api, win32con
win32api.MessageBox(win32con.NULL, '本程序需要以管理员权限运行才能正常使用！', '提示')
os._exit(0)
'''

import win32api,win32con,win32com,win32com.shell.shell,pythoncom
import os,sys,traceback,time,shutil,threading,re,requests,json,re,base64,configparser,glob,datetime,string,argparse
import tkinter.messagebox as messagebox
import tkinter as tk

parser=argparse.ArgumentParser(description="更新程序")
parser.add_argument("-c",help="指定渠道打包")
