import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write_byte('\0')
</code>
But this only works if the file is opened in binary mode. In the example above, a <code>bytes(1)</code> object is created, which contains the integer value 1, but this is an actual integer, not the character <code>\0</code>.

