from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'xcbB11s'
s.size = s.format.size
s.pack = s.format.pack
s.unpack = s.format.unpack

pack = Struct('xcbB11s').pack
unpack = Struct('xcbB11s').unpack

print unpack(pack(1, 'hello', True))
</code>
output:
<code>(1, 'hello', True)
</code>
In your example, the struct object's format string is <code>'xcbB11s'</code> and the first element after <code>&lt;class '_struct.Struct'&gt;</code> is its <code>format</code> attribute.

