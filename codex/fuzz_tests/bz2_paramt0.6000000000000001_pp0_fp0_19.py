from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed)

# Class for 'with' statement
class closing(object):
    def __init__(self, obj):
        self.obj = obj
    def __enter__(self):
        return self.obj
    def __exit__(self, *args):
        self.obj.close()

# Make a temp file that auto-deletes
import os
import tempfile
with closing(tempfile.TemporaryFile(dir=os.getcwd())) as f:
    f.write('blah')

# Get the size of a directory
import os
os.path.getsize('/path/to/file')

# Get the size of a file
import os
os.path.getsize('/path/to/file')

# Get the size of a directory
import os
os.path.getsize('/path/to/file')

# Get the size of a file
import os
os.path.getsize('/path/to/file')

# Get the size of a directory
import os
os.path.getsize('/
