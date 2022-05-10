import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I'm getting the following error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I'm using Python 3.6.1 on Windows 10.
I've tried reading the documentation, but I can't figure out what I'm doing wrong.
I'm expecting the <code>m[:]</code> to return an empty byte array, but instead it's throwing an error.


A:

The documentation for <code>mmap.mmap</code> states:
<blockquote>
<p>If <code>&lt;code&gt;mmap&lt;/code&gt;</code> is used to map an empty file, <code>&lt;code&gt;mmap&lt;/code&gt;</code> will create a memory-backed file of the specified <code>&lt;code&gt;length&lt;/code&gt;</code>. If <code>&lt;code
