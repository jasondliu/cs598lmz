import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    buf = m.read_byte()
    assert buf == b'\x01', buf
    m.write_byte(b'\0')
    m.seek(0)
    buf = m.read_byte()
    assert buf == b'\0', buf
    print('{!r}'.format(buf))
</code>
The result is:
<code>'\x00' # expected value
</code>

