import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1, access=mmap.ACCESS_WRITE)
    m[:] = b'A'
</code>
There's no <code>truncate</code> call and all I can see that might be implicitly forcing a file modification is <code>f.write</code>, but I didn't see a way to make that write anything that might provoke a file modification without actually writing to the file. I noticed that the mmap raises an exception if you try to write 'out of bounds' of the file, which I'm hoping is a result of the mmap refusing to write beyond the file's current size. But perhaps the mmap is doing something else behind the scenes that causes file updates.
In any case, I don't want the file updates to occur. I'm trying to avoid file system operations so that I can test the program I'm writing in memory environments so that I don't have to deal with file permissions issues. And I also don't want to have to change anything in the python code that uses the mmap in production, since it's very widely used in the codebase, so I can't just change the open statements to include the <code>O_DIRECT</code> flag
