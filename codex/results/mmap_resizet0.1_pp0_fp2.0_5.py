import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I don't understand why I get this error. I thought that the mmap object would be updated when the file is truncated.
I am using Python 3.6.4 on Windows 10.


A:

The documentation for <code>mmap.mmap</code> says:
<blockquote>
<p>The <em>length</em> argument specifies the number of bytes to map. The entire file is mapped if <em>length</em> is omitted or is <code>&lt;code&gt;0&lt;/code&gt;</code>.</p>
</blockquote>
So you are mapping the entire file, which is now empty.
You can use <code>mmap.resize</code> to resize the mapping.

