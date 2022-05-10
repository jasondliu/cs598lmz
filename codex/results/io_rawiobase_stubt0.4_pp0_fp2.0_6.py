import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n)
    def readinto(self, b):
        data = self.file.read(len(b))
        n = len(data)
        try:
            b[:n] = data
        except TypeError as err:
            import array
            if not isinstance(b, array.array):
                raise err
            b[:n] = array.array('b', data)
        return n

def _get_encoder(encoding):
    if encoding == 'utf-8':
        return codecs.getencoder('utf-8')
    return codecs.getincrementalencoder(encoding)

def _get_decoder(encoding):
    if encoding == 'utf-8':
        return codecs.getdecoder('utf-8')
    return codecs.getincrementaldecoder(encoding)

def _get_reader(stream, encoding, errors):
    if encoding ==
