import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get this error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I can work around this by seeking to the end of the file before truncating:
<code>f.seek(0, 2)
f.truncate()
</code>
... but that seems like a hack.
Is there a better way to truncate a file that's mmapped?

