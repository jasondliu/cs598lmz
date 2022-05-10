import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[1] = bytes(1)
</code>
This throws:
<blockquote>
<p>OSError: [Errno 22] Invalid argument</p>
</blockquote>
I have been poking around with this for some time, and I can see why it would complain, but I can't find out how to do what I want.


A:

You can't <code>mmap</code> more than the actual file size, you will have to resize the file.
<code>with open('test', 'r+b') as f:
    f.seek(0, os.SEEK_END)
    f.write(bytes(1))
    f.truncate()

    m = mmap.mmap(f.fileno(), 0)
    m[1] = bytes(1)
</code>

