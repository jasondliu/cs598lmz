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
If I run this code on linux with python 3.6 and 3.7, <code>a</code> is <code>b''</code>. But on windows 10 with python 3.6, it is <code>b'\x01'</code>. Why is this?


A:

From https://docs.python.org/3.7/library/mmap.html#mmap.mmap:
<blockquote>
<p>On Windows, <code>&lt;code&gt;mmap&lt;/code&gt;</code>ing a file opened in text mode has unexpected results. Use binary mode instead.</p>
</blockquote>

