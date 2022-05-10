import codecs
codecs.register (search_function)

from ctypes import *
lib_path = os.path.dirname(__file__) + '/hmdx.dll'

class FileIOException(Exception):
    """Exception when file can't be open or read from"""

class InvalidFileException(Exception):
    """Exception when invalid file format is given as input"""

class HashFileIterator(object):
    """Iterate through the data in a .hash file"""

    def __init__(self, file):
        """Initialize the iterator, check the file is OK and get ready to iterate"""

        self.file = file
        self.position = 0

        if not self.CheckMagic():
            raise InvalidFileException("File is not a hash file")

        self.hash_table_length = self.ReadUInt32()
        self.num_hashes = self.ReadUInt32()
        self.num_blocks = self.ReadUInt32()

        self.file.seek(self.hash_table_length + 0x10)

    def __iter__(self):
        return self
