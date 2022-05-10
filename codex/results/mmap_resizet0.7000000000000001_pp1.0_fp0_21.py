import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This prints the value <code>b'\x01'</code> (the byte <code>1</code>), but I was expecting an empty result, since <code>f.truncate()</code> should have removed the byte. What am I missing?


A:

You're not missing anything. You're just misunderstanding how the <code>mmap</code> module works.
From the documentation:
<blockquote>
<p>The mmap constructor creates a memory-map to an existing file. It is also possible to map an entire device into memory.</p>
</blockquote>
So when you create a memory map, it doesn't matter what you then do to the file. The memory map will still contain whatever data was in the file when you created it.
If you want to truncate a file and then read from it using <code>mmap</code>, you need to create a new memory map after truncating the file.

