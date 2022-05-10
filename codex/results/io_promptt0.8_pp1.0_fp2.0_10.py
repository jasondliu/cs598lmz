import io
# Test io.RawIOBase.readall
print (io.RawIOBase.readall.__doc__)

with open('jalape\xf1o.txt', 'w') as f:
    f.write('spicy')

with open('jalape\xf1o.txt', 'rb') as f:
    print (f.readall())

# The following example works on both 32-bit and 64-bit systems
# because the size is stored in a C long, which is always 32 bits.
with open('/dev/urandom', 'rb') as f:
    print (f.read(5))

# Test io.RawIOBase.readinto
import io
print (io.RawIOBase.readinto.__doc__)

with open('jalape\xf1o.txt', 'rb') as f:
    b = bytearray(5)
    n = f.readinto(b)
    print (repr(b))
    print (n)

# Test io.RawIOBase.readline
import io
print (io.RawIOBase.readline
