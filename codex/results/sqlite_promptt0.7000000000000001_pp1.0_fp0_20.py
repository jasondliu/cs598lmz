import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('test.db', timeout=3)

def get_file_size(file_path):
    if os.path.isfile(file_path):
        file_path_size = os.path.getsize(file_path)
        return file_path_size
    else:
        return 0


def get_file_md5(file_path):
    if os.path.isfile(file_path):
        md5 = hashlib.md5()
        f = open(file_path, 'rb')
        md5.update(f.read())
        hash_code = md5.hexdigest()
        f.close()
        md5 = str(hash_code).lower()
        return md5
    else:
        return ""


def get_lib_path(lib_name):
    lib_name = ctypes.util.find_library(lib_name)
    return lib_name


def get_file_sha1(file_path):
    if os.path.isfile(file_path):
        sha1 = hashlib.sha
