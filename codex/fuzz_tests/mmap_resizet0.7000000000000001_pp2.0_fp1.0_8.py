import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code throws a segmentation fault.
I'm not sure if I'm doing something wrong or if it's a bug in python.
I'm running python 3.4 on ubuntu 14.04.

