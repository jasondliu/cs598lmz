import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print a
    m.close()
</code>
Is it possible to truncate the file and read the old content from the mmap?
I'm getting this error:
<code>Traceback (most recent call last):
  File "mmap_test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>

