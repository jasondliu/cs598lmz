import ctypes
import ctypes.util
import threading
import sqlite3
import json
import os.path

def lib_get():
    """
    returns the ctypes handle to the nfc-binding
    """
    libnfc_path = ctypes.util.find_library("nfc")
    if libnfc_path is None:
        libnfc_path = "libnfc.so"
    return ctypes.cdll.LoadLibrary(libnfc_path)

libnfc_handle = lib_get()

def libnfc_version():
    """
    returns the libnfc version string
    """
    return libnfc_handle.nfc_version()
    
def init(conf_path=None):
    """
    initialize the libnfc library
    """
    if conf_path is None:
        conf_path = os.path.dirname(__file__) + "/libnfc.conf"
        if not os.path.isfile(conf_path):
            conf_path = "/etc/nfc/libnfc.conf"
    c_conf_path = ctypes.create_string
