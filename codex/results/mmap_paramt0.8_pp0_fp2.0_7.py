import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1)
    m[0] = bytes(2)
    m.flush()
    print(m)
    print(f.read())
</code>
So this is a file with size 1 that was written with a 0 and the code first gets a memory map with mmap and then changes the first byte to a 2 and the prints out the memory map and the file.
However, when I run this from the terminal with python3.5, it prints out the file as bytes(1) when it should be bytes(2)
<code>posix_ipc$ python3.5 mmap_not_working.py 
&lt;mmap.mmap object at 0x7fac236a4e80&gt;
b'\x02'
</code>
This only happens if I use mmap. If I remove the mmap part and just write to the file, the file is bytes(2) as it should be
<code>posix_ipc$ python3.5 mmap_not_working.py 
b'\x01'
b'\x01'
</code>
Is this a bug in
