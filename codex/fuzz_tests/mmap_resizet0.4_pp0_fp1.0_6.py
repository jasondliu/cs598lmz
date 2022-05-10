import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This will raise <code>ValueError: mmap offset is greater than file size</code>.
Is there a way to truncate the file without invalidating the mmap?
I know I can close the mmap first and then truncate the file, but I would like to avoid that since I have a lot of code that would have to be changed.

