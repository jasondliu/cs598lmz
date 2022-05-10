import bz2
bz2.decompress(compressed_data)
# 'This is the original text.'

import zlib
s = 'witch which has which witches wrist watch'
print len(s)

t = zlib.compress(s)
print len(t)

zlib.decompress(t)

zlib.crc32(s)

import binascii

binascii.crc32(s)

#Shallow and Deep Copies
import copy
class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)



bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)

id(bus1), id
