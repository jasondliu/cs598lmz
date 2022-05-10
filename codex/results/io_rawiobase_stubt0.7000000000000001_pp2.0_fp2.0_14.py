import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        pass

def open(name, mode, buffering):
    return File(name, mode)


# Python 2.6

from __future__ import with_statement

import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        pass

def open(name, mode, buffering):
    return File(name, mode)

class File_2_6(io.IOBase):
    def __init__(self, filename, mode):
        pass

def open_2_6(name, mode, buffering):
    return File_2_6(name, mode)


# Python 2.6, but with io.open

from __future__ import with_statement

import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        pass

io.open = open

def open(name, mode, buffering):
    return File(name, mode)

class File_2_6(io.
