import io
class File(io.RawIOBase):
    '''
    File object

    Attributes
    ----------
    name : str
        Path to file
    mode : str
        File mode
    file : file
        Internal file object
    '''
    def __init__(self, name, mode='r'):
        '''
        Constructor

        Parameters
        ----------
        name : str
            Path to file
        mode : str, optional
            File mode
        '''
        super(File, self).__init__()
        self.name = name
        self.mode = mode
        self.file = None

    def __enter__(self):
        '''
        Open file
        '''
        self.file = open(self.name, self.mode)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        '''
        Close file
        '''
        self.file.close()

    def readable(self):
        '''
        Check if file is readable
        '''
        return self.file.writable()

    def writ
