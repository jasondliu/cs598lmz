from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<3s3sHH'
s.size = 3*2+2*2 #14
print(s.size)

# from mutable byte sequence to immutable bytes
b1 = b'\x01\x02\x03\x04'
u1 = u1.encode('utf-8') # turn the unicode string into bytes
print(u1)
b1 #<bytes>: b'\x01\x02\x03\x04'

# read untis into a buffer and then use memoryview to view the contents of the buffer in various formats
with open('sunset.jpg', 'rb') as f:
    tag_bytes = f.read(3) # read 3 bytes
    print(tag_bytes)
    # JPEG
    m1 = memoryview(b1) #<memoryview>: <memory at 0x7ffa9d5719d8>
    m1.tolist() #[1, 2, 3, 4]
    m1.tobytes() #b'\x01\x02\x03\x04
