import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The python docs about file objects imply that a call to <code>truncate</code> should also truncate the mmap, as the file object is the source of the mmap. But the behaviour I see is that the file is truncated, but the mmap happily reads data past the end of the file.
If I move the mmap map call to after the truncate then the mmap is truncated, but that is not an option for me. Is it possible to get the expected behaviour of truncate truncating the mmap as well?

