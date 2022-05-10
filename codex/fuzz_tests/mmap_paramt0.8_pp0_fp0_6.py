import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[:])
    print(m[:])
    print(m[:])
    print(m[:])
    print(m[:])
    print(m[:])
    print(m[:])
    print(m[:])
    print(m[:])
    m.close()

</code>
Whenever I try to read the file, the program seems to hang, but only if I try to read the file multiple times. Any help would be greatly appreciated!


A:

Your problem is that you are calling <code>print(m[:])</code> multiple times in a loop. <code>mmap</code> objects are already iterable, so you don't need to call <code>m[:]</code> at all. Just try this instead:
<code>print(m)
</code>
and you will get the expected result.
Your code works if you use Python 3.8.2. I'm guessing you're using an old Python version. The reason for this is that <code>mmap</code> objects in Python 3.8.2
