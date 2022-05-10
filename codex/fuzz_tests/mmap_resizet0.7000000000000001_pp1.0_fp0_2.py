import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
When i try to access the array, python gives me the following error:
<blockquote>
<p>mmap.error: [Errno 22] Invalid argument</p>
</blockquote>
How can i fix this?
I'm using Python 3.6.2


A:

The problem is that you're reading from the file after you've truncated it. (You truncate it by calling <code>f.truncate()</code>; that happens before you read from the file.) The documentation says you get <code>mmap.error</code> when <code>mmap()</code> fails, and the underlying C code says it fails when the file size is zero.
The documentation also says that <code>mmap()</code> "disconnects the underlying file object from the file descriptor", but that's not the problem here, because <code>mmap()</code> doesn't actually close the file until you release it, and you didn't release it.
The solution is, don't truncate the file until after you're done reading and writing.

If you need to truncate the file for
