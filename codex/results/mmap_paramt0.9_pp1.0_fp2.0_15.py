import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    b'1' in m
    b'2' in m
</code>
I expected the last line to return false but it returns True. How is this possible?
I found out that this only happens when the position of the file descriptor is not 0. So the line:
<code>f.seek(1)
</code>
causes this behaviour. 

