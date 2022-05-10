import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.write(b'\x00')
    m.close()
</code>
This does not raise an exception, but the file remains the same.

I'm using Python 3.4.2, but I have tried this on Python 2.7.9 and Python 3.5.0 as well, and the result is the same.
I'm using Windows 7.


A:

You're not writing to the file.
<code>with open('test', 'wb') as f:
    f.write(bytes(1))
</code>
This creates a file with one byte in it.
The byte is <code>0x01</code>.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.write(b'\x00')
    m.close()
</code>
This opens the file and maps it into memory. It then overwrites the byte in the file with <code>
