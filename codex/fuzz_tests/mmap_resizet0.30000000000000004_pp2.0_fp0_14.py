import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I would expect the last line to raise an exception, but it doesn't.
I can't find any documentation on this. Is this a bug?


A:

The documentation for <code>mmap</code> does not say anything about truncating the file.
<blockquote>
<p>The mmap() function is supported on all Unix and Windows systems. On
  Windows, it is only supported on NTFS.</p>
</blockquote>
The documentation for <code>truncate</code> says:
<blockquote>
<p>On Windows, the file-like object must be opened in binary mode, not
  text mode.</p>
</blockquote>
So it seems that <code>truncate</code> is not supported on Windows in text mode.

