import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I would expect <code>a</code> to be <code>b''</code>.
Is there a way to get the expected behavior?


A:

You need to resize the mmap object after truncating the file:
<code>m.resize(0)
</code>

