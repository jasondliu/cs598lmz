from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('hhl')
s.pack(1,2,3)

s.unpack(_)

s.unpack_from(_,4)

s.unpack_from(_,8)

s.pack_into(_,8,1,2,3)

s.pack_into(_,0,1,2,3)

s.pack_into(_,4,1,2,3)

_[4:]

_[4:] == s.pack(1,2,3)

_[4:] == s.pack(1,2,4)

_[4:] == s.pack(1,2,3)

_[4:] == s.pack(2,2,3)

s.unpack_from(_,0)

s.unpack_from(_,4)

s.unpack_from(_,0)

s.unpack_from(_,4)

s = Struct('xcb')
s.size

s.pack(1,2)

s.unpack
