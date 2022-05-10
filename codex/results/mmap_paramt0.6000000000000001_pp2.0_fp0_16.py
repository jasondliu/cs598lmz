import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
    m.close()
</code>
Output:
<code>$ python3.3 mmap.py
$ hexdump -C test
00000000  00                                                |.|
</code>

