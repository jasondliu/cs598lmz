import io
# Test io.RawIOBase
# issue: https://github.com/facebookresearch/torchbeast/issues/59
import pdb

#---------------------------------------------------------------------
# Test functions
#---------------------------------------------------------------------

# Test 1:
# Reading a file descriptor directly, without buffering
def read_fd_1():
    f = open('/mnt/data/text8', 'rb')
    r = io.RawIOBase(f)
    r.seek(0)
    byte = r.read(1)

# Test 2:
# File descriptor opened as buffered
def read_fd_2():
    f = open('/mnt/data/text8', 'rb')
    r = io.BufferedReader(f)
    r.seek(0)
    byte = r.read(1)
    # The read should throw an exception
    # Exception: 'readinto() should not be called on a closed stream'

#---------------------------------------------------------------------
# Run tests
#---------------------------------------------------------------------

