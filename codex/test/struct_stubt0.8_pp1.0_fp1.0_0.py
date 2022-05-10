from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'xcbB11s'
s.size = s.format.size
s.pack = s.format.pack
s.unpack = s.format.unpack

pack = Struct('xcbB11s').pack
unpack = Struct('xcbB11s').unpack

