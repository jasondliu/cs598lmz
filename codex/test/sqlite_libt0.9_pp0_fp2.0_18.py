import ctypes
import ctypes.util
import threading
import sqlite3


from ctypes import *
from ctypes.wintypes import *
import sys
from os import getcwd
from os import listdir
from os.path import isfile, join
import os
from shutil import copyfile
from socket import gethostname
def GetModuleBase(h_process, moduleName): # libbpg.dll
    try:
        Enum_Modules_From_Process_Handle(h_process)
        for base_addr in module_bases:
            if module_bases[base_addr] == moduleName:
                return base_addr
        return False
    except:
        return False

def GetModuleEnd(h_process, moduleName):
    try:
        Enum_Modules_From_Process_Handle(h_process)
        for base_addr in module_bases:
            if module_bases[base_addr] == moduleName:
                return module_ends[base_addr]
        return False
    except:
        return False

