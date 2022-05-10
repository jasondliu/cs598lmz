import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
It turns out that <code>a</code> is still <code>b'\x01'</code> although I truncated <code>f</code>. If I reopen it, truncate, and read again, it will be an empty byte string. But if I reopen the file, truncate and use <code>mmap</code> to access the memory again, there's still <code>b'\x01'</code>. I want to make it an empty byte string as well. How can I do this?
If I use <code>os.ftruncate</code> to truncate the file, I can make the memory slice from <code>mmap</code> be an empty byte string. But I want to know what happens in the file object's truncate method


A:

The Python 2.7 docs for <code>file.truncate</code> says:
<blockquote>
<p>truncate() resizes the file to the specified size. It returns the new size.</p>
</blockquote>
The Python 3.6 docs are a bit more explicit
