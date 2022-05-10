import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('shop.db')

def path_example():
    print("This is right path: ", ctypes.util.find_library('README.txt'), "\n")
    print("This is wrong path: ", ctypes.util.find_library('README'), "\n")
    

class MyThread(threading.Thread):
    def __init__(self, libpath):
        threading.Thread.__init__(self)
        self.libpath = libpath
        self.clib = ctypes.CDLL(self.libpath)

    def run(self):
        if os.path.exists(self.libpath):
            self.clib.somelibfun()
        else:
            print('File not found!')


class MyThread1(threading.Thread):
    def __init__(self, libpath):
        threading.Thread.__init__(self)
        self.libpath = libpath
        self.clib = ctypes.CDLL(self.libpath)

