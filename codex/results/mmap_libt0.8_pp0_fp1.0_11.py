import mmap
import os
import re
import subprocess
import sys
import tempfile
import time

def prc(cmd):
    print(cmd)
    if sys.platform.startswith('win'):
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE
        subprocess.Popen(cmd, startupinfo=startupinfo, shell=True)
    else:
        subprocess.Popen(cmd, shell=True)

def easy_grep(pattern, files_to_check):
    for file in files_to_check:
        try:
            with open(file, 'r+b') as f:
                s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
                if s.find(pattern) != -1:
                    return True
                else:
                    return False
        except:
            return False

def easy_text_grep(pattern
