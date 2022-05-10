import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(2)
</code>


A:

The problem is that you're passing an <code>int</code> to the <code>bytes</code> constructor.  When you do this, it's interpreted as the size of the byte array you want.  Instead, you want to pass a <code>str</code> (which is what you get from <code>bytes</code> when you index it).  You can do this with <code>chr</code>:
<code>m[0] = chr(2)
</code>

