import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(len(m))
    print(m.read_byte())
    m.write_byte('\x02')
    print(m.read_byte())
</code>
output:

1
1
2

The file is still at 1 byte, despite the output text.
This is on Python 3.7.3.
Is this a bug, or is there some explanation for this?
Thanks.

