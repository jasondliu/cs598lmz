from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('&lt;I')
print(s.pack(50))
</code>
Now for your purpose, don't do this. Instead use the <code>io</code> module:
<code>import io
import _struct

s = _struct.Struct('&lt;I')

b = io.BytesIO()
s.pack_into(b, 0, 50)
print(b.getvalue())
</code>

