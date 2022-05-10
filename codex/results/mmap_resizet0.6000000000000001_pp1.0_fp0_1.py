import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code results in an <code>OSError: [Errno 22] Invalid argument</code> on the line <code>a = m[:]</code>.
I am running Python 3.6.6 on Windows 10.
Why is this happening?


A:

The <code>mmap</code> module documentation clearly states that:
<blockquote>
<p>If the file is opened for update, any changes made to the memory are
  also written back to the file.</p>
</blockquote>
So when you truncate the file, the contents of the mmap become undefined (and accessing it triggers the exception you see).

