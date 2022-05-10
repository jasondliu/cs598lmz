import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I got "ValueError: cannot mmap an empty file".
I am not sure if I was too strict on the definition of "file pointer".
Maybe you should try the above code snippet, just to make sure.

