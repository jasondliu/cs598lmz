import bz2
bz2.BZ2File.read = my_read
bz2.BZ2File.readline = my_readline

# Fix for bz2.BZ2File.seek()
def my_seek(self, offset, whence=0):
    if whence == 1: # SEEK_CUR
        offset = self.tell() + offset
    elif whence == 2: # SEEK_END
        offset = self.size + offset
    if offset < 0:
        offset = 0
    if offset > self.size:
        offset = self.size
    self.pos = offset
bz2.BZ2File.seek = my_seek

# Fix for bz2.BZ2File.seekable()
def my_seekable(self):
    return True
bz2.BZ2File.seekable = my_seekable

# Fix for bz2.BZ2File.tell()
def my_tell(self):
    return self.pos
bz2.BZ2File.tell = my_tell

# Fix for bz2.B
