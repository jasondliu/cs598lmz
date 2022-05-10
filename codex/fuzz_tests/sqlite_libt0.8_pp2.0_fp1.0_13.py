import ctypes
import ctypes.util
import threading
import sqlite3
import os

g_bInit = False
g_Dll = None
g_hServer = 0
g_hDb = 0
g_bNeedUninit = False
g_bServerStarted = False
g_SocketLock = None

g_CbConnect = None
g_CbDisconnect = None
g_CbRecv = None
g_CbSend = None
g_CbError = None

def __InitDll():
    global g_Dll
    g_Dll = ctypes.CDLL(ctypes.util.find_library("ServerDll"))
    g_Dll.Init.argtypes = []
    g_Dll.Uninit.argtypes = []
    g_Dll.StartServer.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
    g_Dll.StopServer.argtypes = []
    g_Dll.SendData.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c
