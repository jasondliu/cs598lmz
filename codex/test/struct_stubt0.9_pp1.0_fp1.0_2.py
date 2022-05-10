from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<10s10s')

pack = s.pack
unpack = s.unpack
pack('Hello')

unpack('Hello')
