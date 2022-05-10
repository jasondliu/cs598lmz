import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.write_byte(bytes(1))
    m.write_byte(bytes(2))
    m.write_byte(bytes(3))
    m.seek(0)
    m.write_byte(bytes(5))
    m.close()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 13, in &lt;module&gt;
    m.write_byte(bytes(1))
TypeError: write_byte() argument must be int, not bytes
</code>
I do not understand why. I tried different things (I just want to write a byte) but it does not work. What could be the problem?

