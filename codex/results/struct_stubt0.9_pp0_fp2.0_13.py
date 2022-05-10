from _struct import Struct
s = Struct.__new__(Struct)
s.error = error
s.pack = pack
s.pack_into = pack_into
s.unpack_from = unpack_from
s.unpack = unpack
if hasattr(Struct,"iter_unpack"):
    s.iter_unpack = Struct.iter_unpack
i = Struct.__new__(Struct)
i.error = error
i.pack = pack
i.pack_into = pack_into
i.unpack_from = unpack_from
i.unpack = unpack
if hasattr(Struct,"iter_unpack"):
    i.iter_unpack = Struct.iter_unpack
l = Struct.__new__(Struct)
l.error = error
l.pack = pack
l.pack_into = pack_into
l.unpack_from = unpack_from
l.unpack = unpack
if hasattr(Struct,"iter_unpack"):
    l.iter_unpack = Struct.iter_unpack
q = Struct.__new__(Struct)
q.error = error
q.pack = pack
