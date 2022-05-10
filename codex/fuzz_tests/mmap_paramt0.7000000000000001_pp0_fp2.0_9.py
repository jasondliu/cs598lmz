import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.write_byte(b'2')
    m.close()
</code>
The first <code>open</code> creates the file and writes a byte. The second <code>open</code> opens the file and creates a memory map from it. The memory map allows you to access the file as if it were in memory and it allows you to change the contents of the file.
Here's the output of <code>hexdump -C test</code> before:
<code>00000000  01                                                |.|
</code>
And here's the output of <code>hexdump -C test</code> after:
<code>00000000  32                                                |2|
</code>

