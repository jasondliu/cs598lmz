import ctypes
import ctypes.util
import threading
import sqlite3
import codecs

# Python 3 compatability
try:
    unicode
except NameError:
    unicode = str

class LibraryLoader(object):
    '''Dynamic library loader for ctypes'''
    def __init__(self):
        self.other_libnames = []

    def load_library(self, libname):
        '''Given the name of a library, load it.'''
        paths = []

        if os.path.isabs(libname):
            paths.append(libname)
        else:
            # Why? Because if we enter "libzmq" it's the same as "libzmq.so"
            # on Unix and "libzmq.dll" on Windows.
            if not libname.startswith('lib'):
                libname = 'lib' + libname
                # If the extension is not specified, we add it based on the
                # current platform.
                if os.name == 'nt' and not libname.endswith('.dll'):
                    libname += '.dll'
                elif not lib
