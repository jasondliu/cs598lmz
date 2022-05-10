import codecs
# Test codecs.register_error() and handle replacement characters properly.

def open1(filename, mode='r', encoding='ascii'):
    f = codecs.open(filename, mode, encoding)
    f.codec_info = (encoding, codecs.getencoder(encoding),
                    codecs.getincrementalencoder(encoding),
                    codecs.getdecoder(encoding),
                    codecs.getincrementaldecoder(encoding))
    return f

def open2(filename, mode='r', encoding='ascii'):
    f = codecs.open(filename, mode, encoding)
    f.codec_info = (encoding, codecs.getencoder(encoding),
                    codecs.getincrementalencoder(encoding),
                    codecs.getdecoder(encoding),
                    codecs.getincrementaldecoder(encoding))
    def reader(f):
        while 1:
            s = f.readline()
            if s:
                yield s.replace("a", "")
            else:
                break
    f.
