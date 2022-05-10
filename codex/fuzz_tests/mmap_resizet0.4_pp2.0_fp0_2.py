import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code prints <code>b'\x01'</code> on Python 3.6.3, but <code>b''</code> on Python 3.7.0.
I guess it is because of some changes in mmap module.
Is there any way to get the content of mmap object after truncating the file?


A:

This is not a bug.
<blockquote>
<p>Is there any way to get the content of mmap object after truncating the file?</p>
</blockquote>
No.
<blockquote>
<p>I guess it is because of some changes in mmap module.</p>
</blockquote>
No, it's because of changes in the underlying operating system.
<blockquote>
<p>This code prints b'\x01' on Python 3.6.3, but b'' on Python 3.7.0.</p>
</blockquote>
It's not a bug. It's a feature.
The behaviour of <code>mmap</code> has not changed. What has changed is the behaviour of
