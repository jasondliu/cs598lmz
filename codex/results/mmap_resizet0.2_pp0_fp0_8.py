import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
The last line raises an exception:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I'm using Python 3.5.2 on Windows 10.
Why does this happen?
How can I avoid it?


A:

The problem is that the <code>mmap</code> object is not aware of the truncation.
The <code>mmap</code> object is a wrapper around the <code>mmap</code> C function. The documentation for that function says:
<blockquote>
<p>The <code>&lt;code&gt;mmap()&lt;/code&gt;</code> function is not part of the C library, but is a system call implemented by the operating system. The <code>&lt;code&gt;mmap()&lt;/code&gt;</code> function is not aware of any changes made to the file after the <code
