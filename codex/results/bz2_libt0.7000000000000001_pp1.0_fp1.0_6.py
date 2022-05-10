import bz2
bz2.decompress(bz2.compress(bytes('Hello World!', 'utf-8')))

import gzip
gzip.decompress(gzip.compress(bytes('Hello World!', 'utf-8')))


class Log:
    def __init__(self, filename):
        self.filename = filename

    def write(self, message):
        f = open(self.filename, 'a')
        f.write(message + '\n')
        f.close()

    def close(self):
        pass


import contextlib

@contextlib.contextmanager
def log(filename):
    f = open(filename, 'a')
    try:
        yield f
    finally:
        f.close()

with log('example.txt') as f:
    f.write('Hello World!')


# __enter__() and __exit__() must be implemented
class Log():
    def __init__(self, filename):
        self.filename = filename

    def write(self, message):
        f = open(self.filename, '
