from bz2 import BZ2Decompressor
BZ2Decompressor()

class TextReader(object):
    def __init__(self, path):
        self._path = path
        self._file = None
        self._decoder = None

    def __enter__(self):
        self._file = open(self._path, 'rb')
        self._decoder = codecs.getincrementaldecoder('utf-8')('ignore')
        return self

    def __exit__(self, type, value, traceback):
        self._file.close()
        return False

    def __iter__(self):
        return self

    def __next__(self):
        line = self._file.readline()
        if len(line) == 0:
            raise StopIteration()

        data = self._decoder.decode(line)
        return data.rstrip('\r\n')

    def next(self):
        return self.__next__()

def main():
    import argparse
    from docopt import docopt
    from dsutil.multiprocessing import Pool

    def fn(name, reader
