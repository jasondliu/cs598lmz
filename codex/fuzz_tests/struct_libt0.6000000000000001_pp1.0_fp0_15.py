import _struct
import _io
import subprocess
import platform
import tempfile
import shutil
import re

def _get_buffer_size(fd):
    '''
    Gets the buffer size of a file descriptor.
    '''

    try:
        size = _fcntl.fcntl(fd, _fcntl.F_GETPIPE_SZ)
    except AttributeError:
        size = _fcntl.fcntl(fd, _fcntl.F_GETPIPE_SZ, 0)

    return size

class Pipe:
    '''
    A class that interfaces with a pipe.
    '''

    def __init__(self, parent, r, w, mode):
        self.parent = parent
        self.r = r
        self.w = w
        self.mode = mode

        # Get the buffer size
        self.buffer_size = _get_buffer_size(self.w)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
       
