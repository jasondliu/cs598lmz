import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
It gives me an error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I don't understand why I can't get the data from the <code>mmap</code> object. I can still do <code>m.tell()</code> and <code>m.seek(1)</code>, so the object still exists.


A:

<code>mmap</code> is a mapping to the file descriptor, not the current file contents.
The file descriptor is still open, so you can still read it, but it is empty.
If you need to map a file that you are editing, you need to do it in a different way.
One way would be to open the file, <code>map</code> the file, then <code>truncate</code> the file.
Another way would be to <code>map</code> the file, then <code>truncate</code> the file descriptor.

