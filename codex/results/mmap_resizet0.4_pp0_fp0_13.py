import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
I understand that the error is raised because the file is truncated and the mmap object doesn't know about it.
I would like to know if there is a way to tell the mmap object to "refresh" its memory map.
I know I can use <code>mmap.seek(0)</code> to go to the beginning of the file, but I don't know if there is a way to know how many bytes are mapped.
I could use <code>mmap.size()</code> but I don't know if it will return the size of the file or the size of the mapped region.
I could also use <code>mmap.tell()</code> to get the current position, but I don't know if it will return the position in the file or the position in the mapped region.
I could also use <code>mmap.seek(0, os.SEEK_END)</code> to go to the end of the file, but I don't know if it will go to the end of the file or the end of the
