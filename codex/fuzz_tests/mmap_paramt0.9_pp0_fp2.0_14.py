import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read(1)) # b'\x00'
</code>
Except that I would be surprised if <code>mmap()</code> still accepted zero as size, although it may or may not. It certainly did at one time, anyway.
Also, as mentioned in a comment, another way of achieving this is by <code>mapping.seek(position)</code> to the specified position (e.g. <code>0</code>). For files that just accept bytes, that would work fine but is not recommended (since it deviates from the behaviour of reading from a regular file).
Regarding making a read-only <code>mmap</code>, I think you're going to be disappointed. I found Python mmap - creating read-only sub-region, but it doesn't look promising to me.

