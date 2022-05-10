import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)
</code>
Output:
<code>b''
</code>
I was expecting to see an empty string, but I was wrong. I also tried to use <code>mmap.ACCESS_READ</code> instead of <code>0</code>, but it also doesn't work.
Does anybody know why does it work like this? Is there any way to fix it?
UPD:
I was wrong, I was expecting to see the empty string, but it was <code>b'\x00'</code>. 


A:

The docs say:
<blockquote>
<p>When <code>&lt;code&gt;mmap&lt;/code&gt;</code> is used in <code>&lt;code&gt;MAP_SHARED&lt;/code&gt;</code> mode, the file may not actually grow until <code>&lt;code&gt;msync()&lt;/code&gt;</code> or <code>&lt;code&gt;munmap()&lt;/code&gt;</code> is
