import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = ord('a')
    m.close()
</code>
This code works great on Mac OS X, but fails on Linux with the following error:
<code>mmap.error: [Errno 22] Invalid argument
</code>
I am using Python 3.5.1 on both systems.


A:

The problem is that <code>mmap.mmap()</code> requires that the file is opened in read/write mode.  On Linux, <code>f.write(bytes(1))</code> is not enough to open the file in read/write mode.  You need to do <code>f.write(bytes(1))</code> and then <code>f.flush()</code>.
For more information, see https://stackoverflow.com/a/2333872/1399279

