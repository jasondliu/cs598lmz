from _struct import Struct
s = Struct.__new__(Struct)   
s.endian = "="
s.format = "L"
s.size = 4
</code>
and then I can use methods such as <code>s.pack()</code> and <code>s.unpack()</code> for serialization and deserialization.  I found that this solution has the same effect as importing <code>struct</code> using <code>from _struct import *</code>.


A:

The <code>_struct</code> module is implemented in C, as indicated by the leading underscore. This means that its behavior is necessarily a bit different than the rest of the standard library. The <code>struct</code> module is a Python implementation, so is a more natural fit for the standard library.

