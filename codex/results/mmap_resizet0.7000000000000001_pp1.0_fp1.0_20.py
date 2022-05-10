import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)
</code>
I expected this to print <code>[]</code>, but it segfaults instead.
I watched this in <code>strace</code>, and it happens after the last mmap function, <code>mmap(NULL, 64, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0)</code>.
How do I fix this?

