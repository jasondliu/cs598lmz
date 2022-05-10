import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)
</code>
So the question is if this is pythonic and if there is a better way for this?


A:

This looks fine if the string is created with f.truncate() before reading the mmap. 

