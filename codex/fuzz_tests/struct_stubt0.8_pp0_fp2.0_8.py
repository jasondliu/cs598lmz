from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('&gt;2h')
s.unpack_from(data, 1)
</code>
This outputs: <code>(20, 10)</code>.

