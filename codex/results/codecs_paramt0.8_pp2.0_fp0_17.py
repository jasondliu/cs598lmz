import codecs
codecs.register_error('strict', codecs.lookup_error('utf-8'))

class Reader(object):
    def __init__(self, fname, mode='r', encoding='utf-8'):
        self._fname = fname
        self._mode = mode
        self._encoding = encoding
        self._handle = codecs.open(self._fname, self._mode, self._encoding, 'strict')
        self._line = ''
        self._read_line()

    def __iter__(self):
        return self
    
    def __del__(self):
        self._handle.close()

    def close(self):
        self._handle.close()
        self._handle = None

    def _read_line(self):
        line = self._handle.readline()
        if line:
            self._line = line.strip()
        else:
            self._line = None

    def next(self):
        """
        Reads next line from file
        """
        if self._line is None:
            raise StopIteration
        line =
