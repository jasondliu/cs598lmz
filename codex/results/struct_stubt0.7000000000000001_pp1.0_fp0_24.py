from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__.update(Struct.__dict__)
s.format = 'I I I I'
s.size = s.calcsize(s.format)

fmt = Struct(s.format)

for i in range(5):
    rand_bytes = os.urandom(40)
    print(rand_bytes)
    bytes_out = fmt.pack(*rand_bytes)
    print(bytes_out)
    print(fmt.unpack(bytes_out))
    print(fmt.unpack_from(bytes_out, 0))
</code>


A:

The <code>I</code> format in struct is for integers, which are four bytes long.
<code>os.urandom(40)</code> generates 40 random bytes. <code>I</code> will try to unpack 4 bytes, but the first four bytes of the 40 byte string are not an integer.
I think you want <code>s.format = '40s'</code> instead.

