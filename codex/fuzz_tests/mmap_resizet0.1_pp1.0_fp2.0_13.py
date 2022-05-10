import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I would expect the <code>mmap</code> object to be updated when the file is truncated. Is there a way to do this?


A:

You can't do this.  The mmap object is a view of the file at the time it was created.  It doesn't change when the file changes.  If you want to change the file, you need to close the mmap object and reopen it.

