import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
The last line of the above code throws an exception
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I would like to know if there is a way to get the data from the mmap object after the file is truncated.


A:

The <code>mmap</code> object is tied to the file size, so when you truncate the file, the <code>mmap</code> object can no longer access the data.
From the docs:
<blockquote>
<p>The mmap() function provides a simple way of memory-mapping a file.
  This is a convenient way to access a file’s contents without reading
  the entire file into memory.</p>
<p>The mmap() function is used to create a new memory-mapped file object.
  The file must be opened in one of the following modes:</p>
<ul>
<li>
