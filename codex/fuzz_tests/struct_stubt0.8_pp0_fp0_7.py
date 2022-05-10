from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = calcsize(s.format)
print s.size
print s.format

def get_int(data):
    return s.unpack(data)[0]
import struct, cPickle

def new_load(fp):
    r_id = struct.unpack('>I', fp.read(4))
    return cPickle.load(fp)

def new_dump(obj, fp):
    fp.write(struct.pack('>I', len(obj)))
    cPickle.dump(obj, fp, cPickle.HIGHEST_PROTOCOL)
from twisted.internet import reactor
from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineReceiver

class EchoClient(LineReceiver):
    end="Bye-bye!"

    def connectionMade(self):
        self.sendLine("Hello, world!")
        self.sendLine("What a fine day it is.")
        self.sendLine(self.end)

    def line
