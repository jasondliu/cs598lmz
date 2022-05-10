import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I'm getting an error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I can't understand why, because I'm not changing the offset of the mmap object. I'm just changing the size of the file.
I'm using Python 3.6.0 on Windows 10 x64.


A:

The <code>mmap</code> module is not really intended for use with a file that is being extended.  The <code>mmap</code> object is linked to a specific region of the file, and if you extend the file, the region it was linked to is no longer valid.
The documentation for the <code>mmap</code> module says:
<blockquote>
<p>Note that modifications to the file while it is mapped will not be reflected in the contents of the mmap object unless the modified portions are also mapped. If the file is changed by another process while it is mapped, the result is undefined and may cause
