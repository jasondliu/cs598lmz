from _struct import Struct
s = Struct.__new__(Struct)
s.format = "hhl"
s.size = 8
b = b"\x01\x02\x03\x04\x05\x06\x07\x08"

nd =  b[:s.size*n]
nd

# unpack the buffer
res = np.asarray(s.unpack(nd))
print(res)

# test if byte order is correct
print(res == a)
</code>
<blockquote>
<p>[1 2 987654321]</p>
<p>[ True  True  True]</p>
</blockquote>

