import mmap
import sys

#
# 
#
class MMapFile(object):
    """
    MMapFile class
    """
    def __init__(self, filename, mode='r', access=mmap.ACCESS_WRITE):
        """
        Constructor
        """
        self.filename = filename
        self.mode = mode
        self.access = access
        self.mmap = None
        self.file = None
        self.open()

    def open(self):
        """
        Open the file
        """
        self.file = open(self.filename, self.mode)
        self.mmap = mmap.mmap(self.file.fileno(), 0, access=self.access)

    def close(self):
        """
        Close the file
        """
        self.mmap.close()
        self.file.close()

    def read(self, length=0):
        """
        Read the file
        """
        if length == 0:
            return self.mmap.read()
        else:
            return self.mm
