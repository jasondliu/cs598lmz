import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(2)
</code>
This works as expected. But if I add a <code>mmap.ACCESS_READ</code> flag to the <code>mmap</code> call:
<code>m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m[0] = bytes(2)
TypeError: mmap can't modify a readonly memory map.
</code>
I'm on Python 3.6.2.
My question is: why? What's the point of the <code>mmap.ACCESS_READ</code> flag?


A:

As the documentation states:
<blockquote>
<p>The optional <code>&lt;code&gt;access&lt;/code&gt;</code> parameter determines whether write access to the underlying file will be allowed. The default is <
