import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
But I have an error in the last line: <code>OSError: [Errno 22] Invalid argument</code>. 
I think that I can't read from the map after truncation and I have to close the map, open the file again, and create the new map. But I want to do this without closing and opening the file. Is it possible?


A:

You can't. The <code>mmap</code> can't be resized. You should close the file and reopen it.

