import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Traceback:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: cannot read from closed file
</code>
I think that at the moment of creating mmap, the file descriptor is referenced in mmap object, and it is closed at the moment of truncate. Is there a way to truncate the file and keep the mmap object valid?

