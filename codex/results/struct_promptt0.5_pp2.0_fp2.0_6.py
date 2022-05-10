import _struct
# Test _struct.Struct methods
#
# Structs can be created in two ways:
#
#    >>> from _struct import *
#    >>> s = Struct('i')
#    >>> t = Struct('hhh')
#
# or
#
#    >>> s = Struct('i')
#    >>> t = Struct('hhh')

#    >>> s = Struct('i')
#    >>> s.size
#    4
#    >>> t = Struct('hhh')
#    >>> t.size
#    6

#    >>> s = Struct('i')
#    >>> s.pack(1)
#    '\x01\x00\x00\x00'
#    >>> t = Struct('hhh')
#    >>> t.pack(1,2,3)
#    '\x01\x00\x02\x00\x03\x00'

#    >>> s = Struct('i')
#    >>> s.unpack('\x01\x00\x00\x00')
#    (1,)
#    >>> t = Struct('hhh')
#    >>> t.un
