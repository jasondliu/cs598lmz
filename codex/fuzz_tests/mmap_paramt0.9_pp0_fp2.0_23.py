import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0:1] = b'1'
    m[0:1].decode()
</code>
Is there a way?


A:

Yes, the Windows version of mmap() does not support changing the underlying file size. So, m.resize(2) will fail with errno 22 (EINVAL).
Bytes (and nums) in the range 0-127 are equal to their unicode representation. So, you can use <code>m[0]</code> directly. It will give you a str char, exactly as you desired (see below).
<code>&gt;&gt;&gt; m = mmap.mmap(1,1,access=mmap.ACCESS_WRITE)
&gt;&gt;&gt; m
&lt;mmap.mmap object at 0x04273600&gt;
&gt;&gt;&gt; m[0]=1
&gt;&gt;&gt; m[0]
49
&gt;&gt;&gt; type(m[0])
&lt;type 'str
