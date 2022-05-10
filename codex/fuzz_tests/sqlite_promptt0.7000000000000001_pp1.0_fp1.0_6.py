import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/home/mike/Desktop/Python/pythontesting/test.db')

libc_path = ctypes.util.find_library('c')
libc = ctypes.CDLL(libc_path)

def get_piped_input(pipe, size):
    """
    Get input from the pipe, limited to the maximum number of bytes.  Returns a
    tuple of the input and the number of bytes read.
    """
    buf = ctypes.create_string_buffer(size)
    if libc.read(pipe, buf, size) == -1:
        raise IOError('get_piped_input: error reading from pipe')
    return buf.value, ctypes.sizeof(buf)

def get_output(cmd, size):
    """
    Get output from the given command.  Returns a tuple of the output and the
    number of bytes read.
    """
    pipe_read, pipe_write = os.pipe()
    pid = os.fork()
    if pid == 0:
        # Redirect stdout to the pipe.
       
