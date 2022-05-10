import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I expected to get an empty list, but instead I get a list of bytes with a single element equal to 1.
I thought that after truncating the file, the mmap object is no longer valid, but apparently I'm wrong.
I'm using Python 2.7.


A:

<blockquote>
<p>From the docs</p>
<p>Any changes to the file object’s position attribute are reflected in the mmap object’s view, and vice versa. If the file is extended, the extra data is not visible in the mmap object’s view. If the file is truncated the extra data is removed from the view. The mmap object has no way of knowing if the underlying file has been changed by another process. It is the responsibility of the programmer to flush changes to disk and to update the mmap object when the file has been updated by another process</p>
</blockquote>
So you can do this in your code:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', '
