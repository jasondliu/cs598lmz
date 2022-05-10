import io
class File(io.RawIOBase):
    def __init__(self, file):
        super(File, self).__init__()
        self.file = file
    def read(self, size=-1):
        return self.file.read(size)
    def readall(self):
        return self.file.readall()
    def readinto(self, b):
        data = self.file.read(len(b))
        n = len(data)
        b[:n] = data
        return n

#
#
#

from collections import namedtuple
from types import SimpleNamespace

class _Namespace(namedtuple('_Namespace', 'name value')):
    def __new__(cls, name, value):
        return super(_Namespace, cls).__new__(cls, name, value)

class _NamespaceArray(namedtuple('_NamespaceArray', 'name value')):
    def __new__(cls, name, value):
        return super(_NamespaceArray, cls).__new__(cls, name, value)

class _
