import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = m[0]

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[0])
</code>
And the output is:
<code>0
</code>
After reading, the value is not preserved. I checked the man page, but found nothing about it. Is this a normal behavior?


A:

Yes, it is normal behavior.
The <code>mmap</code> object is an abstraction that makes a file look like a contiguous array of bytes. You can manipulate those bytes, but the changes are not committed until you call <code>mmap.flush()</code>. And as of today, there is no way for <code>mmap</code> to know that you changed the value at index <code>0</code>, so you should explicitly tell it to flush that byte.
For example:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = m
