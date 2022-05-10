from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x00\x00\x00\x00')

# b'\x00\x00\x00\x00' is a bytes object, which is iterable over integers
# (the bytes). So this is equivalent to:
s.unpack(iter(b'\x00\x00\x00\x00'))
</code>
The <code>unpack</code> method in turn calls <code>self._unpack_from</code>, which calls <code>self._unpack</code>. <code>_unpack</code> is defined as:
<code>def _unpack(self, buf):
    for obj in self._iterunpack(buf):
        return obj
</code>
So it iterates over <code>self._iterunpack(buf)</code>, and returns the first value. <code>_iterunpack</code> is defined as:
<code>def _iterunpack(self, buf):
    offset = 0
    for field in self.format:
        size =
