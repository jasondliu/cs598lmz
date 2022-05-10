import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
If I don't <code>m.close()</code> before <code>f.truncate()</code>, the program raises:
<code>Traceback (most recent call last):
  File "test.py", line 11, in &lt;module&gt;
    m = mmap.mmap(f.fileno(), 0)
mmap.error: [Errno 22] Invalid argument
</code>
How come a closed file descriptor can still be used to create a valid mmap object?
Please note that I'm using python 2.6 for historical reasons.


A:

I assume that <code>f.fileno()</code> returns the same file descriptor before and after the truncation.
If this is true, this is expected behavior.
<code>mmap.mmap()</code> takes a file descriptor, not a file object, so it doesn't care what you do to the file object.
The fact that the file descriptor is no longer associated with the file object is irrelevant. You can even open a new file object that uses the same file descriptor, but this won't affect the <
