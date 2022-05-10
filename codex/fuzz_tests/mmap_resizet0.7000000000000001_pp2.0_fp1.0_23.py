import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code should read a byte from the file, truncate it, and print the byte. It seems as if the mmap is not keeping track of what is going on with the underlying file. Is this a bug or am I misunderstanding how mmap works?


A:

You need to call <code>m.close()</code> before doing anything to the file.  If you don't, the changes you make to the file are not reflected in the mmap.

