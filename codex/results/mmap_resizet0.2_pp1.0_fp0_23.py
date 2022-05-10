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
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I understand that the mmap object is pointing to the old file size, but I don't know how to fix it.
I've tried calling <code>m.resize(0)</code> but that doesn't work.
I've tried calling <code>m.close()</code> and then reopening the file, but that doesn't work either.
I've tried calling <code>m.seek(0)</code> and then <code>m.resize(0)</code>, but that doesn't work either.
I've tried calling <code>m.seek(0)</code> and then <code>m.close()</code>, but that doesn't work either.
I've tried calling <code>m.seek(0)</code> and then <code>m.close()</code> and then reopening the file, but that doesn't work
