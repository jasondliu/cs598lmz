import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
</code>
In Python 3, this results in the following error:
<code>Traceback (most recent call last):
  File "test.py", line 6, in &lt;module&gt;
    m = mmap.mmap(f.fileno(), 0)
ValueError: mmap length is zero
</code>
What is the error here?


A:

<code>f.write(bytes(1))</code> only creates one byte, of value 0.
You can double-check this by adding:
<code>print(m.read(2))
</code>
And you will see '\x00'.
Try: <code>f.write(bytes((7,)))</code>.

