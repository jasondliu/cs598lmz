import mmap
import socket
import struct
from StringIO import StringIO

# Read
def read(path):
    f = open(path, 'r')
    data = f.read()
    f.close()
    return data

# Write
def write(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

# Data Reader
class DataReader(StringIO):
    def readInt8(self):
        return self.getByte()
    def readInt16(self):
        return self.getShort()
    def readInt32(self):
        return self.getLong()
    def readInt64(self):
        return self.getLong()
    def readUInt8(self):
        return self.getByte()
    def readUInt16(self):
        return self.getShort()
    def readUInt32(self):
        return self.getLong()
    def readUInt64(self):
        return self.getLong()
    def readChar(self):
        return self.
