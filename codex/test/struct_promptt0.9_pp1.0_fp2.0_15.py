import _struct
# Test _struct.Struct using the formatted string.
TestError( _struct.calcsize('=') != 0, "calcsize('=') != 0")
TestError( _struct.calcsize('<') != 0, "calcsize('<') != 0")
TestError( _struct.calcsize('>') != 0, "calcsize('>') != 0")
TestError( _struct.calcsize('=') != _struct.calcsize(''), "calcsize('=') != calcsize('')")
TestError( _struct.calcsize('=') != _struct.calcsize('i'), "calcsize('=') != calcsize('i')")

# Test the code size increasing bug.  This bug used to be found in _struct.py
# as well as setup.py before it was fixed.
class X(object):
    def __init__(self):
        self.x = 1

TestError( X().x != 1, "X().x != 1")

s = "12345678"
