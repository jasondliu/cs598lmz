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
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I would expect the <code>mmap</code> object to be updated when the file is truncated.
I'm using Python 3.6.5 on Windows 10.


A:

The <code>mmap</code> object is not updated when the file is truncated.
The documentation says:
<blockquote>
<p>The mmap() function is supported on Windows and Unix, and is available on all platforms that support the Python mmap module. The mmap() function is available in Python 2.2 and later.</p>
</blockquote>
The documentation also says:
<blockquote>
<p>The mmap() function is supported on Windows and Unix, and is available on all platforms that support the Python mmap module. The mmap() function is available in Python 2.2 and later.</p>
</block
