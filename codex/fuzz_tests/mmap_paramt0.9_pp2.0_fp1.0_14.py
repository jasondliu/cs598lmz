import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] == 1
</code>
However this does work in Python 2 and all the examples I've seen so far have been in Python 2... so I have no idea what's going on here. Any idea how to make this code work or at least know why it doesn't work?
Update:
Apparently (though it wasn't mentioned anywhere in Python 3 documentation) the type of mmap's constructor changed so the second argument is no longer the access type but dimension:
<code>mmap(fileno, size, access=ACCESS_DEFAULT, offset=None)
</code>
In the Python 2 documentation:
<code>mmap(fileno, length[, flags[, prot[, access[, offset]]]])
</code>
So this code works in Python 3:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1)
    print(m[0])
</code>
which is weird... I would expect a warning about the deprecation or even an error.


A:

According to the Python 3 Doc
