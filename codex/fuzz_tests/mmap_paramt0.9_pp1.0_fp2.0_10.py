import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read_byte())
    m.seek(0)
    m.write_byte(b'B')
</code>
thanks.


A:

Seems to me it's the <code>mmap</code> rather than Python that's the problem here, judging from https://github.com/python/cpython/blob/2.7/Modules/mmapmodule.c#L448
It's a safeguard -- probably written when <code>mmap</code> was still new, before it was as tightly integrated as it is today -- to ensure that you're writing to a file, not something like <code>/dev/kmem</code> or some other special character device. (The check runs both for normal Python <code>mmap</code> and the <code>mmap</code> support built into io.FileIO.)

