import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%

import sys

def print_sys_info():
    print("Python version: {}".format(sys.version))
    print("Python version info: {}".format(sys.version_info))
    print("Python executable: {}".format(sys.executable))
    print("Python prefix: {}".format(sys.prefix))
    print("Python path: {}".format(sys.path))

print_sys_info()

#%%

import os

def print_os_info():
    print("OS name: {}".format(os.name))
    print("OS type: {}".format(os.uname()))
    print("OS environ: {}".format(os.environ))
    print("OS getcwd: {}".format(os.getcwd()))
    print("OS getcwdb: {}".format(os.getcwdb()))
    print("OS getlogin: {}".format(os.getlogin()))
    print("OS getpid: {}".format(os
