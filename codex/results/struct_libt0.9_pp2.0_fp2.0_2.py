import _struct as struct
import codecs
import ctypes

import math

def get_game_funcs_in_process(process_name):
    # Get target process
    pi = win32process.EnumProcesses()
    foundProcess = None
    for p in pi:
        try:
            h = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, False, p)
            try:
                n = ntdll.NtQueryInformationProcess(h, ntdll.ProcessImageFileName)[1].name.lower()
                #if n.startswith("csgo.exe"):
                if n.endswith(process_name.lower()):
                    foundProcess = p
                    break
            finally:
                win32api.CloseHandle(h)
        except win32process.error:
            pass
    if foundProcess != None:
        mfh = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, False, foundProcess)
        # Get all modules in the process
        modules = win32process.
