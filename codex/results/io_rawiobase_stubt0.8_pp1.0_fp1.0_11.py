import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def fileno(self):
        return self.f.fileno()
    def read(self, n):
        return bytes(self.f.read())
    def seekable(self):
        return self.f.seekable()
    def seek(self, offset, whence=0):
        return self.f.seek(offset, whence)
    def close(self):
        self.f.close()

def file(f):
    return File(f)


################################################################
# working with directories

import resources
import os

def listdir(path='.'):
    return os.listdir(path)

def mkdirs(path, mode=0o777):
    os.makedirs(path, mode)

def mkdir(path, mode=0o777):
    os.mkdir(path, mode)

def chdir(path):
    os.chdir(path)

def getcwd():
    return os.getcwd()

def stat(path
