import ctypes
ctypes.windll.shell32.IsUserAnAdmin()

#https://stackoverflow.com/questions/1823058/how-to-check-if-current-script-is-running-as-root-or-sudo
import os
import sys

if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")

#https://stackoverflow.com/questions/1369526/what-is-the-python-keyword-with-used-for
class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

#https://stackoverflow.com
