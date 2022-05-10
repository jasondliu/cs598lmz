import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file::memory:?cache=shared')

class CdbFile(object):
    '''
    A class for iterating through the records of a cdb file.
    '''

    def __init__(self, cdbfile, readonly=True):
        '''
        Initialize a new CdbFile object.

        @type cdbfile: file-like object
        @param cdbfile: a file-like object containing a cdb file.
        @type readonly: bool
        @param readonly: if true, the CdbFile will be opened read-only
        '''
        self.cursor = 0
        self.readonly = readonly
        self.cdbfile = cdbfile
        self.cdbfile.seek(0)
        self.cdblib = ctypes.CDLL(ctypes.util.find_library('cdb'))
        if self.readonly:
            self.cdblib.cdb_init.argtypes = [ctypes.c_void_p, ctypes.c_int]
            self.cdblib.
