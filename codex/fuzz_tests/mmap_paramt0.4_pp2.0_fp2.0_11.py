import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read_byte())
    m.write_byte(bytes(1))
    m.seek(0)
    print(m.read_byte())
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    m.write_byte(bytes(1))
TypeError: write_byte() argument must be int
</code>
The write_byte method expects an int, but I am passing it a byte. What am I doing wrong?


A:

The <code>bytes</code> constructor expects an iterable of integers, not a single integer. If you want to create a single-byte <code>bytes</code> object, use the <code>bytes</code> constructor with a single integer parameter:
<code>m.write_byte(bytes(1))
</code>

