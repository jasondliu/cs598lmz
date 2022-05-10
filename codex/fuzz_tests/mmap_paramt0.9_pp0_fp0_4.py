import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[0])
</code>
It works, but only if I specify the sizes for both <code>f.write</code> and <code>mmap.mmap</code>
Is it possible to achieve the same functionality when the buffer is dynamically created?


A:

The <code>mmap</code> module works because different objects in Python can sometimes share a memory block. On top of that, Python 3 uses Unicode strings internally and the "memoryview" class implements low-level, block-based access to a string's underlying bytes which absolutely can be mapped over the host system's virtual memory to give actual access to file contents, the same way a <code>bytes()</code> or <code>bytearray()</code> would. Here's an example, which uses the <code>lru_cache()</code> decorator to efficiently cache a file with a certain size on the heap, rather than map it over a file every time. I assumed that you are on a Unicode-aware platform, and use the Unicode C-API, but that's an easy thing to change to a <code>bytes()</code> or <
