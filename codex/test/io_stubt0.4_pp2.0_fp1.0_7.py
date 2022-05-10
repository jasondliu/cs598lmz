import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

# This is a regression test for a bug in the io module:
# When a BufferedReader was closed, it would not close the underlying
# raw stream, if the latter was a file.

# The bug was triggered by the following sequence of events:
# - a BufferedReader was created, with a file object as the raw stream;
# - the BufferedReader was closed, but the file was not;
# - the file was closed.
#
# When the file was closed, it would call the close() method of its
# buffer object, which was the BufferedReader object.  The BufferedReader
# object would then try to close its raw stream, which was the file.
# The file was already closed, so the close() method would raise a ValueError.

# The regression test is as follows:
# - create a BufferedReader, with a file object as the raw stream;
# - close the BufferedReader;
# - close the file.
#
# If the bug is present, the file's close() method will raise a ValueError.

# The bug is fixed in Python 2.6.


