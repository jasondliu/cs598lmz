import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()

print(a)
</code>
I have tried to add <code>f.flush()</code> before <code>truncate()</code> but <code>a</code> is still set to 1.
<code>a</code> should be an empty byte string but it is not.
Is there a way to fetch the updated file content after truncating it?


A:

Using the <code>mmap</code> module means that you're using the operating system's memory-mapping interface. As the name suggests, you're mapping a file into memory and accessing it via the memory. You see what's in memory, not what's on the disk.
You need to <code>mmap.close()</code> your <code>mmap</code> object and then <code>flush()</code> the file to get the file updated on disk.

