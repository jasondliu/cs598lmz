import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(0)
</code>
I get the following <code>TypeError</code>:
<code>Traceback (most recent call last):
  File "mmap_test.py", line 9, in &lt;module&gt;
    m[0] = bytes(0)
TypeError: must be read-write buffer, not mmap
</code>
However, when instead of the last 2 lines I write:
<code>m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
m[0] = bytes(0)
</code>
It works flawlessly. Does this mean <code>mmap</code> does not provide read-write buffers until <code>access=mmap.ACCESS_WRITE</code> is specified?


A:

You are mapping it as read-only. The default <code>access</code> value is never writeable, see the documentation:
<blockquote>
<p><code>&lt;code&gt;access&lt;/code&gt;
