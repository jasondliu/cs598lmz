import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

def get_libc():
    libc_path = ctypes.util.find_library('c')
    if not libc_path:
        raise Exception('libc not found')
    libc = ctypes.CDLL(libc_path)
    return libc

def get_thread_id():
    libc = get_libc()
    return libc.syscall(186)

def get_thread_name():
    return threading.current_thread().name

def get_thread_info():
    return (get_thread_id(), get_thread_name())

def get_thread_info_str():
    return '{} ({})'.format(*get_thread_info())

def print_thread_info():
    print(get_thread_info_str())

def get_thread_info_callback(connection, cursor, user_data):
    connection.create_function('get_thread_info', 0, get_thread_info)
