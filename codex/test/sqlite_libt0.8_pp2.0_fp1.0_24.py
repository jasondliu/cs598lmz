import ctypes
import ctypes.util
import threading
import sqlite3
import datetime
import os



def get_lib(libname):
    return ctypes.cdll.LoadLibrary(ctypes.util.find_library(libname))

def get_err_msg():
    return ctypes.get_errno()

def set_err_msg(err_no):
    ctypes.set_errno(err_no)

def get_err_code():
    return ctypes.get_errno()

def get_thread_ident(thread_id):
    return threading.current_thread().ident

def set_thread_ident(thread_id):
    threading.current_thread().ident = thread_id

# # # # # # # # # # # # # # # # # # # # # # # #
#                                             #
#   DATABASE NAME                              #
#                                             #
# # # # # # # # # # # # # # # # # # # # # # # #


def set_db_name():
    return ':memory:'

