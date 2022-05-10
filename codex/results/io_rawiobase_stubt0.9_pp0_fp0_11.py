import io
class File(io.RawIOBase):
    '''\
    The File class is for all intents and purposes a drop-in replacement for io.FileIO.
    It also caches, so if the OS fails to write, all writes after the OS write failure can be cached and then retried.
    '''
    def __init__(self, name, mode='r', buffering=None, read_mode=None, write_mode=None, cache_size=0, cache_seconds=0):
        if(name == ''):
            raise ValueError
        if(not os.path.isfile(name)):
            filename = os.path.abspath(name)
            filepath = filename[:filename.rfind(os.sep)]
            if(os.path.exists(filepath)):
                raise IOError
            os.makedirs(filepath)
            f = open(name, "ab+")
            f.close()
        self.__actual = io.FileIO(name, mode)
        self.__name = name
        self.__mode = mode
        self.__cache_size = int
