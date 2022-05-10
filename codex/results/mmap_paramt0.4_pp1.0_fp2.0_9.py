import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(1))
    m.seek(0)
    print(m.read(1))
</code>
I'm getting this error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m.write(bytes(1))
TypeError: write() argument must be a bytes-like object, not 'int'
</code>
Why is this happening?

