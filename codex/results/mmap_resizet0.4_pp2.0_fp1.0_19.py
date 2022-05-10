import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()
</code>
The error is:
<code>Traceback (most recent call last):
  File "test.py", line 11, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
How can I get the current bytes in the file?


A:

The problem is that you are using <code>mmap</code> to map the entire file, but you then truncate the file. From the docs:
<blockquote>
<p>The mmap() function returns a mmap object of size <code>&lt;code&gt;length&lt;/code&gt;</code> bytes</p>
</blockquote>
So you've mapped the entire file, but then you truncated the file to 0 bytes.

Instead, you should use <code>mmap.resize</code> to resize the mapping. From the docs:
<blockquote>
<p>Resize the memory mapping, possibly moving its contents. The new size must not be larger than the file
