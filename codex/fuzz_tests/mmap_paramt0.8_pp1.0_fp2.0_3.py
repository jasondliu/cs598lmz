import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'abc')

with open('test', 'rb') as f:
    print(f.read())
</code>
As you can see, this is a very early stage of a very simple library, which I would like to expand. The library will be used in my own programs, too, so I will take care that everything works as expected.
I have read that using <code>mmap</code> may lead to race conditions and segfaults (especially when using multiple threads) when using <code>file.write()</code> at the same time. I tried to figure out how to avoid this problem, but I fear that I may not have understood everything correctly.
I think that the main issue may be that the file handles passed to the <code>mmap</code> objects (and later to the serialization functions) may be closed, which could lead to a segfault in the library. If this is the case, I will just make sure to pass the file handles to the library, because the user may not be able to get them for whatever reason.
The other issue may be the access to the <code>mmap
