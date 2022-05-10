import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    f.flush()
    b = m[:]
    f.flush()
    c = m[:]
    m.close()
    f.close()

print(a)
print(b)
print(c)
</code>
My question:
Is the behavior I get expected? Is it a bug? What would be the correct way to do this?
I don't want to use <code>mmap.MMAP_NORESERVE</code> because then I will get <code>ValueError: mmap can't resize memory maps backed by files</code> when I try to resize my memory map.

