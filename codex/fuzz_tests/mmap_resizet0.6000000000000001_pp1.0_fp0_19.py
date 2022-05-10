import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The code above will produce an exception (in python 2.7), but in python 3.4, it will not. Moreover, in python 3.4 the <code>a</code> variable will contain the value <code>b'\x00'</code> instead of <code>b'\x01'</code>.
Is there any reason for this behaviour? I read the documentation and found nothing. I also checked the source code, but it was too cryptic for me.
Note: I don't want to use <code>mmap.resize</code>, because it is not implemented on my platform.

