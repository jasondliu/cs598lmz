import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("file::memory:", check_same_thread=False)
# and it will work even if the connection is used by different threads.
#
# sqlite3.connect("file::memory:", check_same_thread=False)
sqlite3.connect("file::memory:", check_same_thread=False)

# This example only works on Windows and if ctypes.CDLL("SDL2.dll") is working.
# (It didn't work for me.)
#
# https://stackoverflow.com/questions/5692479/how-to-call-a-c-dll-from-python
# https://stackoverflow.com/questions/24281698/ctypes-cdll-load-library-cannot-open-shared-object-file
#
# libc = ctypes.CDLL(ctypes.util.find_library("c"))
# libc.SDL_Init(0)
#
# https://stackoverflow.com/questions/49074091/python-multithreading-with-sdl2-and-pygame

