import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.seek(0)
    m.write(bytes(2))
</code>
I get this error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    m.write(bytes(2))
ValueError: must have exactly one argument
</code>
What is wrong?


A:

I think you are looking for <code>mmap.mmap.write_byte</code>.
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.seek(0)
    m.write_byte(b'\x02')
</code>

