import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m[0] = bytes(2)
</code>
I expected the <code>test</code> file to contain a byte with value 2, but instead it remains with 1. Also the program hangs on the <code>m.close()</code> method (I haven't included it in the code because it doesn't work either).
What am I doing wrong?
Thanks in advance!


A:

<code>m[0] = bytes(2)</code> is trying to store a 2-byte string in position <code>0</code>. But <code>bytes(2)</code> is <code>b'\x00\x00'</code> (two zero bytes). Whereas <code>bytes(1)</code> is <code>b'\x01'</code> (one byte, with the value <code>1</code>), and <code>bytes(13)</code> (for example) is <code>b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x
