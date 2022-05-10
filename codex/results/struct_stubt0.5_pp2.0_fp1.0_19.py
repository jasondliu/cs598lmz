from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4

def unpack(str):
    return s.unpack(str)
</code>
This is a bit of a hack, and I'm sure there's a better way to do this (perhaps by subclassing Struct), but it works.

