import io
class File(io.RawIOBase):
    '''
    Implements a file to read from and write to a 'file' object in memory.
    '''

    def __init__(self, filename=None, mode='rb'):
        '''
        Initializes the file.
        '''
        self.__buffer = b''
        self.__mode = mode
        self.__position = 0
        self.__filename = filename

    def __len__(self):
        '''
        Gets the length of the buffer.
        '''
        return len(self.__buffer)

    def readable(self):
        '''
        Gets whether the file is readable.
        '''
        return 'r' in self.__mode

    def writable(self):
        '''
        Gets whether the file is writable.
        '''
        return 'w' in self.__mode

    def seekable(self):
        '''
        Gets whether the file is seekable.
        '''
        return True

    def close(self):
        '''
        Closes the file.
        '''

