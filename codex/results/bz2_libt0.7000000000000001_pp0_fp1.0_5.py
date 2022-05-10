import bz2
bz2.compress(data).decode('ascii')

# a few bytes of bz2 compressed random data
data = bz2.compress(b'random data')

# the python 3.2 bz2 module doesn't support context managers
import bz2
with bz2.open('file.txt.bz2') as input:
    text = input.read()

# use contextlib to create a context manager for the bz2 module
import contextlib

@contextlib.contextmanager
def open_bz2(filename, mode='rt'):
    """Open a file compressed with bz2.
    """
    # open the file with bz2.BZ2File and yield it
    with bz2.open(filename, mode) as f:
        yield f

with open_bz2('file.txt.bz2') as input:
    text = input.read()

import bz2
with open('file.txt.bz2', 'rt') as input:
    text = bz2.decompress(input.read().
