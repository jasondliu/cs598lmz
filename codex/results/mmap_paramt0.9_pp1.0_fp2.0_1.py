import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    # write a null byte and flush to disk to "truncate" the file
    m.write_byte(b'\x00')
    m.flush()
    # print mapping as string
    print(m.read_byte())
    # print last character in file
    print(m[-1])
</code>
Now I have read_byte method and I was wondering if there is method such as write_bytes that will allow me to write 8 bytes directly to the mmap object.


A:

No, there's no method to write a sequence of bytes (or other data type) to a mapped file.  You can, however, easily create such a function yourself, e.g.,:
<code>from struct import Struct
def write_bytes(memmap, pos, values):
    for v in values:
        memmap[pos:pos+8] = Struct('Q').pack(v)
        pos += 8
</code>
It might be better to make <code>values</code> a <code>bytearray</code> and use <code>ctypes</code> instead of
