import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m)
    m.write(bytes(2))
</code>
The file is created, but I get the following error:
<code>mmap.error: [Errno 22] Invalid argument
</code>


A:

The problem is that you are using the <code>mmap</code> module to map the entire file into memory, but you are not providing the length of the file.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
</code>
You need to provide the length of the file, either by providing a value greater than 0, or by using <code>mmap.ALLOCATIONGRANULARITY</code> as the second argument, which will map the entire file into memory.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), mmap.ALLOCATIONGRANULARITY)
</code>

