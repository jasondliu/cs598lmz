import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

import win32api
import win32con
win32api.MessageBox(win32con.NULL, 'Python 你好！', '你好', win32con.MB_OK)

import win32gui
win32gui.MessageBox(win32gui.GetForegroundWindow(), "Python 你好！", "你好", 0)

import tkinter
tkinter.messagebox.showinfo('Python tkinter', 'Python 你好！')

import wx
wx.MessageBox('Hello wxPython', 'wxPython', wx.OK | wx.ICON_INFORMATION)

import easygui
easygui.msgbox('Hello easygui!', 'easygui', 'OK')
