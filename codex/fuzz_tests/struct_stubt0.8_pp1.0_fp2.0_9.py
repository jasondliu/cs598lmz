from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4

import operator
import types

INT_MAX = 2147483647
INT_MIN = -2147483648

class NumberReader:
    def __init__(self, value):
        assert isinstance(value, (bool, int, float))
        if isinstance(value, float):
            assert value >= -1.0 and value <= 1.0
        self.value = value
        
    def read(self):
        return self.value

class IntReader:
    def __init__(self, value):
        assert isinstance(value, int)
        assert value >= INT_MIN and value <= INT_MAX
        self.value = value
        
    def read(self):
        return self.value

class LongReader:
    def __init__(self, value):
        assert isinstance(value, int)
        self.value = value
        
    def read(self):
        return self.value
    
class FloatReader:
    def __init__(self, value):
        assert
