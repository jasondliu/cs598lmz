import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code prints <code>b'\x00'</code> instead of <code>b'\x01'</code>.
I think that <code>mmap</code> should not be affected by <code>truncate</code>, because it is a separate object.
Is this a bug or am I missing something?
I'm using Python 3.6.5 on Windows 10.


A:

<blockquote>
<p>I think that mmap should not be affected by truncate, because it is a separate object.</p>
</blockquote>
It is not a separate object. It is a view of the file.
<blockquote>
<p>Is this a bug or am I missing something?</p>
</blockquote>
You are missing something.
<blockquote>
<p>The mmap() function is supported on Windows NT, Windows 2000, Windows XP, Windows Server 2003, Windows Vista, and Windows 7. It is not supported on Windows 95, Windows 98, or Windows ME.</p>
</blockquote>
https://docs.python.org/
