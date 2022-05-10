import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I expected the output to be <code>bytes(1)</code> but it's actually <code>bytes(0)</code>. Why is this?
This appears to be OS-dependent as well. On OS X I get a <code>ValueError: mmap length is zero</code>, but on Fedora I get <code>bytes(0)</code>.

