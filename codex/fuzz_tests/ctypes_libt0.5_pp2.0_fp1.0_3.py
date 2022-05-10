import ctypes
ctypes.windll.shell32.IsUserAnAdmin()

#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrator
#
# Created:     20/01/2015
# Copyright:   (c) Administrator 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os,sys,subprocess

def get_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if get_admin():
    pass
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

try:
    subprocess.Popen(r"C:\Program Files\Common Files\Microsoft Shared\TextConv\txtfilt.exe", shell=True)
except:
    pass

def main():
    pass

if __name__ == '__main__':
    main()
