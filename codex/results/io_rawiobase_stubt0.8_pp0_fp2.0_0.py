import io
class File(io.RawIOBase):
    def __init__(self, fname):
        self.fname = fname
        self.file = open(fname, 'rb')

    def write(self, b):
        self.file.write(b)

    def close(self):
        self.file.close()

import sys
class FileWrapper:
    def __init__(self, fname):
        self.file = io.FileIO(fname, 'wb')
        self.size = 0

    def write(self, data):
        self.size += len(data)
        self.file.write(data)

    def __len__(self):
        return self.size

import urllib
def header():
    # ctype,length = dl.info()[:2]
    ctype = 'image/png'
    length = len(FileWrapper)
    print('Content-type: {ctype}\n' \
          'Content-Length: {length}\n\n'.format(**locals()))
    # sys.stderr.write('Content-type
