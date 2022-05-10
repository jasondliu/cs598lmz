import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)

</code>
Is it possible to truncate the file and not discard the data in the mmap? 
Note: I'm doing this because I have a file on disk which I want to mmap to memory, and read the first line in the file to find the size of the file I'm actually interested in.


A:

You can't have read-only mmap of a file that you'll be modifying.
If you could, then you'd have to duplicate the file data just to make the OS call for truncation, since the mmap'd buffer must persist as is until you close it or unmap it from the process space.
Since you're truncating the file immediately after opening it, the mmap size is going to be zero, and you're going to get back a zero-length buffer.
If you want to preserve the data, you could instead just read the first line, <code>seek</code> back to the beginning, then truncate the file using <code>os.ftruncate</code>.

