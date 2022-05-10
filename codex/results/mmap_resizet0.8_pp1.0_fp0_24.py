import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>

OSError: [Errno 22] Invalid argument: b'\x00'

I want to use truncate and keep the mmap.
Is there a way to do it?


A:

Answer is no. You cannot truncate the file while it is mmap'ped.

