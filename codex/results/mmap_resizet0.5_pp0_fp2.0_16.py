import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
It prints <code>b'\x00'</code> instead of <code>b''</code>.
I'm using Python 3.6.1 on Ubuntu 16.04.


A:

I'm not sure why you are getting the result you are getting, but it is not the result I would expect.
The mmap module documentation says:
<blockquote>
<p>After a successful call to mmap(), any changes to the mapped region of the file are reflected in the file.</p>
</blockquote>
So, I would expect that if you truncate the file, the mmap would be truncated as well.

