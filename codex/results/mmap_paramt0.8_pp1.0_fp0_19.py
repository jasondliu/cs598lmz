import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[1:3] = bytes(2)
</code>
The result is <code>b'\x01\x00\x00'</code>.
But I want to write on the bytes that have not been prepared yet.
The result is I want <code>b'\x01\x02\x02'</code>.
How can I fix this?


A:

You can't until you write at least one byte at address 1. 
At that point, you can write more  bytes between adresses 1 and 3.
The size of your file is limited by the available disk space and not by the number of bytes you allocated, so the solution is to always write more bytes than what you need.
I suggest you write more bytes than the maximum size you expect your file to have.

