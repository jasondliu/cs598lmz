from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('Biii')
s.size

# both of these work:
b = s.pack(1, 2, 3, 4)
b = s.pack(b'\1', 2, 3, 4)

# but this doesn't:
b = s.pack(bytes([1]), 2, 3, 4)

# and this doesn't:
b = s.pack(b'\x01', 2, 3, 4)
</code>
In both cases the error is:
<code>TypeError: required argument is not an integer
</code>
I'm using Python 3.6.


A:

The <code>bytes</code> constructor takes a string as an argument.
<code>b = s.pack(bytes('\x01', 'ascii'), 2, 3, 4)
</code>

