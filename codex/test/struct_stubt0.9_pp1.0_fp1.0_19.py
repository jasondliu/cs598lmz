from _struct import Struct
s = Struct.__new__(Struct)
s.size = 88
s.format = 'B b 8s d l d f 33s c'
s.pack_into(buf, 0, 1, 1, b'foobar  ', 3.14, -42, 3.14, 42.5, b'quuxxxxxxxxxxxxxxxxxxxxxxx', ord('a'))
