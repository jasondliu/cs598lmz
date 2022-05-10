import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m[0:1] = bytes(2)
</code>
but it fails with
<code>Traceback (most recent call last):
  File "test_mmap.py", line 6, in &lt;module&gt;
    m[0:1] = bytes(2)
ValueError: cannot modify size of memory mapping
</code>
I've never used <code>mmap()</code> before so I'm curious to know if I'm just doing something wrong, or if there's a better way to do what I'm trying to do, or if there's some fundamental reason why this won't work.


A:

The problem is that you're not allowed to change the size of a memory map (as the error message says).  If you want to change the size of the underlying file, you can do that by changing <code>f.truncate</code> after you've done the <code>mmap</code> call.
Note that you have to change the file size to be larger than the current size, otherwise you'll get an error.
<
