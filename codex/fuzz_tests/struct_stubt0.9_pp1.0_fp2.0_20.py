from _struct import Struct
s = Struct.__new__(Struct)
s.__parse_format__(arg="&gt;I")
s.size
</code>

