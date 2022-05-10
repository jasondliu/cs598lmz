import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.write(bytes(1890))
    m.write(bytes(100))
    m.seek(0)
    out = m.read(20)
    print(out)
</code>
The output is:
<code>b'\x01\x00\x00\x00\x00\x00\x00\x00\xb8\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
</code>
I would expect it to be <code>1901</code> bytes long and the last bytes should be 0x64, but instead it is counted as <code>1890</code> and the last byte is <code>0x00</code>
Why is there no <code>0x00</code> after the 1890 bytes and how do I handle this kind of situation?
PS. If I include <code>len(out)</code> in the last print I get 20 as expected.


A:

This is a
