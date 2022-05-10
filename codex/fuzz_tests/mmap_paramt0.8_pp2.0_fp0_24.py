import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    print(m)

    print(m.write(bytes(1)))

    m.seek(0)
    print(m.read())

    m.seek(0)
    m[0:0] = bytes(1)
    m.seek(0)
    print(m.read())

    m.close()
</code>


A:

The <code>mmap</code> module is a module which allows you to map a file into memory, directly into the memory of your program. 
This means that the changes you make in your program are directly reflected in the file, and vice versa.
The <code>mmap</code> module is also useful for making memory-mapped files, where you can emulate memory as a disk file.
According to the docs:
<blockquote>
<p><code>&lt;code&gt;mmap.ACCESS_WRITE&lt;/code&gt;</code> allows writing to the buffer.</p>
</blockquote>
In your code, you are trying to write to <code>
