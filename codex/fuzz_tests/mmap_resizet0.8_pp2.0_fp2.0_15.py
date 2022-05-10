import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)
</code>
Result:
<code>[]
</code>
This is a little bit strange... Is this behavior by design?


A:

"The contents of the underlying file may be modified at any time, including
when a file or part of a file is mapped." --- From the docs.
This is precisely the reason you will see all manner of "file too short" errors in certain programs when using memory mapped files; a file might be mapped as one size and then later completely re-written.  This use case is not well supported by mmap (although some platforms, like Linux, will try to extend the mapping if possible).
So, the moral of the story is that mmap really does not work well with data files.

