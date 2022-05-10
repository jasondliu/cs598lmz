import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

# MessageBox with Python
from tkinter import messagebox
messagebox.showinfo("Title", "a Tk MessageBox")

# MessageBox with PyQt
from PyQt5.QtWidgets import QMessageBox
msgBox = QMessageBox()
msgBox.setText("The document has been modified.")
msgBox.setInformativeText("Do you want to save your changes?")
msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
msgBox.setDefaultButton(QMessageBox.Save)
ret = msgBox.exec_()

# MessageBox with wxPython
import wx
app = wx.App()
wx.MessageBox('Hello World', 'wx.MessageBox', wx.OK | wx.ICON_INFORMATION)
app.MainLoop()
