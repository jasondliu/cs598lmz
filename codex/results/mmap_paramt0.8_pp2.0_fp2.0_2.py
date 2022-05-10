import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write_byte(0x00)
    m.write_byte(0x01)
    m.seek(0)
    print(m.read_byte())
    print(m.read_byte())
</code>
This is the error I keep getting
<code>Traceback (most recent call last):
  File "E:\Python\mmap_test\test_mmap_writebyte.py", line 10, in &lt;module&gt;
    m.write_byte(0x01)
ValueError: cannot use write_byte on unaligned pane
</code>


A:

<code>m.write_byte</code> writes to a 2-byte word, so it requires the index to be aligned to a word boundary. For example, the following would work:
<code>with open('test', 'wb') as f:
    f.write(bytes(2))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write_byte(0x00
