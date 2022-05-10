import ctypes
import ctypes.util
import threading
import sqlite3
import time
import cProfile
import pstats

db_lock = threading.Lock()

libc_name = ctypes.util.find_library("c")
libc = ctypes.CDLL(libc_name, use_errno=True)

### .data
### .text
### .bss
### .symtab
### .strtab
### .shstrtab
### .debug_line
### .debug_info

def read_struct(f, offset, struct):
        f.seek(offset, 0)
        return struct.from_buffer_copy(f.read(struct.size))

def read_struct_at(f, offset, struct):
        f.seek(offset, 0)
        return struct.from_buffer_copy(f.read(struct.size))

def read(f, offset, size):
        f.seek(offset, 0)
        return f.read(size)

def read_string(f, offset):
        f.seek(offset, 0)
        res = ""
        while True:
                ch =
