import io
# Test io.RawIOBase properties
import io
import sys
import _io

modes = ['r', 'rb', 'rw', 'rwb', 'w+b', 'w+', 'a+', 'a+b']

def read_all(f):
    return f.readall()

def write_all(f, data):
    f.writeall(data)

def internal_buf_size(f):
    if 'r' in f.mode:
        return f.getbuffer().nbytes
    else:
        return f.buffer.nbytes

