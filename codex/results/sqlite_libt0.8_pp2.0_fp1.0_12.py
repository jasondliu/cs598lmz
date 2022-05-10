import ctypes
import ctypes.util
import threading
import sqlite3

sqlite3.register_adapter(decimal.Decimal, str)
sqlite3.register_converter("DECIMAL", decimal.Decimal)

# Import functions that allow us to set the paths to the local shared object libraries
#
def SetLibCPath():
    libc = ctypes.util.find_library("c")
    libc_location = ctypes.util.find_library("c")
    if libc_location:
        file_name = os.path.dirname(libc_location)
        os.environ['LD_LIBRARY_PATH'] = file_name
        print("Using: " + file_name)
    else:
        print("Error: Could not find libc")

def SetLibPamPath():
    libpam_location = ctypes.util.find_library("pam")
    if libpam_location:
        file_name = os.path.dirname(libpam_location)
        os.environ['LD_LIBRARY_PATH'] = file_name
        print("Using:
