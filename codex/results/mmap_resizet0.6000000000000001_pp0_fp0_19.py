import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code prints nothing.
I would like to read the file content before truncate it.
I have tried using <code>os.stat('test')</code> to get the size of the file, but it returns 0.
Is there a way to read the file before truncate ?


A:

The problem is that you are already working with a copy of the file contents, so truncating the file doesn't change the memory-mapped copy.
This is the expected behaviour, because the memory-mapped copy is not a "live" view of the file, but a snapshot.
If you want to continue working with the memory-mapped copy, you can simply truncate it:
<code>m.resize(0)
</code>

