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
ValueError: mmap length is zero
</code>
I would expect that the <code>mmap</code> object would be updated when the file is truncated.
Is there a way to get the <code>mmap</code> object to be updated when the file is truncated?


A:

You can't do that.  The mmap object is a view of the file, and it's not updated when the file changes.  If you want to see the changes, you need to close the mmap object and reopen it.

