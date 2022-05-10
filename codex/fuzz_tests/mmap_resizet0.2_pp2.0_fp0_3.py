import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code works as expected on Linux, but on Windows it raises an exception:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: cannot mmap an empty file
</code>
Is there a way to make this code work on Windows?


A:

The problem is that <code>mmap</code> on Windows will not work with an empty file.
<code>mmap</code> on Windows is implemented using <code>CreateFileMapping</code> and <code>MapViewOfFile</code>.
The documentation for <code>CreateFileMapping</code> says:
<blockquote>
<p>If the specified file is a 0-byte file, the function fails with
  <code>&lt;code&gt;ERROR_FILE_INVALID&lt;/code&gt;</code>.</p>
</blockquote>
The documentation for <code>MapViewOfFile</code> says:
<blockquote>
<p>If the file
