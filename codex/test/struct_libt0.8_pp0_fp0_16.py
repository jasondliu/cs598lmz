import _struct
import __builtin__
try:
    import _struct as __struct
except:
    import struct as __struct
from collections import *
from operator import *
class Block(object):
    __slots__ = ['__iter', '__state', '__len', '__pos', '__len_bits', '__pos_bits', '__buf', '__read', '__write']
    def __iter__(self): return self
    def next(self):
        if self.__pos >= self.__len:
            self.__pos = 0
            raise StopIteration
        else:
            res = self.__iter.next()
            self.__pos += 1
            return res
    def __len__(self): return self.__len
    def __contains__(self, value):
        if not self.__iter:
            while self.__pos < self.__len:
                if not value - self.__iter.next():
                    return True
                self.__pos += 1
