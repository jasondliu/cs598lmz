import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
    m.close()
</code>
This works fine on Linux, but on Windows I get the error
<code>WindowsError: [Error 87] The parameter is incorrect
</code>
What am I doing wrong?


A:

As the documentation for <code>mmap</code> says:
<blockquote>
<p>This module is not supported on Windows. On Windows, mmap cannot be used to map device memory.</p>
</blockquote>

