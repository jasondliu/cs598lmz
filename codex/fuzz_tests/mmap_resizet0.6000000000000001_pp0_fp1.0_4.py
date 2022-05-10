import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
the last line throws the error:
<code>ValueError: mmap length is zero
</code>
However, if I remove the <code>a = m[:]</code> line, the script runs without any error.
How can I fix this?


A:

<code>mmap.mmap()</code> is a memory-mapped file object. It's not a container object. It can only be used to access the file from memory, you cannot use it to read or write the file.
You cannot use the <code>m[:]</code> syntax to get a slice of memory. The only slice syntax you can use is <code>m[0:0]</code> to get a slice of length zero.
If you want to read the file, you need to open it with <code>open()</code> and then read the data from the file object.

