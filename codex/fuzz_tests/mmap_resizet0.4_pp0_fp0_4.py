import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This will raise an error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap slice assignment is wrong size
</code>
Why is this?


A:

The <code>mmap</code> object is a view of the file, not a copy of the file.  If you <code>truncate</code> the file, you're also truncating the <code>mmap</code> object.  You can't assign to a slice of the <code>mmap</code> object because the slice is the wrong size.  The slice is the size of the file, which is 0.

