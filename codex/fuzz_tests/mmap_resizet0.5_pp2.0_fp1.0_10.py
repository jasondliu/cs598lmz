import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This raises the exception:
<code>mmap.error: [Errno 22] Invalid argument
</code>
I understand that the mmap object is now invalid, but is there a way to prevent the exception from being raised? I don't want to have to catch it every time I use the mmap object.


A:

The problem is that the mmap object is not invalidated when the file is truncated. So, when you do <code>m[:]</code>, the mmap object tries to read from the file, but the file is not big enough to hold the data that the mmap object thinks it should hold.
You can fix it by explicitly invalidating the mmap object, like this:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.close()
    a = m[:]
</code>

