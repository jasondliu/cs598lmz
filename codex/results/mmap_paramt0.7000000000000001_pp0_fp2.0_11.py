import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m)

    m.seek(0)
    print(ord(m.read_byte()))

    m.seek(0)
    m.write_byte(bytes(2))

    m.seek(0)
    print(ord(m.read_byte()))
</code>
Outputs:
<code>&lt;mmap.mmap object at 0x7f15a2bef3f0&gt;
1

Traceback (most recent call last):
  File "test.py", line 18, in &lt;module&gt;
    m.write_byte(bytes(2))
TypeError: mmap.write_byte() argument must be int
</code>
The documentation for <code>mmap.write_byte</code> says:
<blockquote>
<p>Write a single byte to the buffer. This is an alias for <code>&lt;code&gt;write()&lt;/code&gt;</code>; it's primarily
  here as a demonstration of the kind of method that can be created for
  use
