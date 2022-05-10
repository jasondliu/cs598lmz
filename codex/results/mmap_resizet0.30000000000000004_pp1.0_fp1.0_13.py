import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This throws an error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I'm guessing this is because the file size is now 0, but the mmap is still pointing to the old location.
Is there a way to update the mmap to point to the new location?


A:

You can't.  The mmap object is now invalid.  You must create a new mmap object.

