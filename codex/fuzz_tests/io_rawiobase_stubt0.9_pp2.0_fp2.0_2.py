import io
class File(io.RawIOBase):
    '''
    This class allows the ease of use of the File object.
    There are two separate "modes" of reading through the file with this class:
    - The "whole" value: The file is read as a whole, presuming that all rows have the same size
    - The "different" value: The file is read per row (values are separated by newline character), allowing different row sizes
    To set these modes, the set_mode(string mode) method can be called, where mode is either "whole" or "different"
    '''
    def __init__(self,name, mode='r', encoding='utf-8'):
        self.file_ptr = open(name, mode, encoding=encoding)
        self._name = name
        self._mode = mode
        self._encoding = encoding
        self._length = 0
        self._mode = "whole"
        self.line = self.file_ptr.readline

    def set_mode(self,mode):
        if mode not in ["whole","different"]:
            raise ValueError("Mode must be either
