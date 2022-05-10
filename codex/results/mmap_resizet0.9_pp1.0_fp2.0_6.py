import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]  # Raises ValueError: Can't extend nonexistent object
</code>
It would be nice if <code>mmap</code> would somehow automatically detect such things, and raise an exception itself.


A:

Unlike other parts of the Python Standard Library, <code>mmap</code> is an extremely thin abstraction over a language feature (memory-mapping) which is natively available.  In this case, it's <code>mmap</code> in the C standard library which <code>mmap</code> in the Python Standard Library is based on.
As such, it does little more than pass your program's input through to it.
If an invalid address or length is being given (as is the case here), the C standard library will raise a <code>SIGBUS</code> or <code>SIGSEGV</code> signal.  The former meaning "Business application error", while the latter means "segmentation error".
In a native program written in C, these signals are "fatal" (the program is terminated); but since they're not used in interpreted programming languages like Python, the C standard library translates them into the "unresolved symbol
