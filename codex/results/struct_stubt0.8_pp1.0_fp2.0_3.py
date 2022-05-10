from _struct import Struct
s = Struct.__new__(Struct)
s.format = '4s4s4s4s'
s.size = 16
</code>
<code>s.unpack</code> will now work as expected.

