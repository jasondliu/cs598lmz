import io
class File(io.RawIOBase):
    def __init__(self,name):
        self.file = open(name,'rb')
        self.size = 1024*1024
        self.buf = b''
        self.tell = self.file.tell
        self.seek = self.file.seek
        self.read = self.file.read
    def readinto(self,b):
        if len(self.buf) < self.size:
            self.size = len(self.buf)
        b = self.buf[:self.size]
        self.buf = self.buf[self.size:]
        return len(b)
    def readable(self):
        return True
    def writable(self):
        return True
    def write(self,b,*args):
        self.buf += b
    def close(self):
        self.file.close()

import csv
f = File('tst.csv')

def read_line(f):
    return [x.decode('cp1252') for x in f.readline().split(b'\t')]

reader
