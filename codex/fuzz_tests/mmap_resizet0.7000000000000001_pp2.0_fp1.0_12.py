import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I know the file is truncated, but I still can get the content of the file by m[:].
I think the content should be empty(maybe some bytes), but in fact, it's still the content before truncate.
Is there a way to make m[:] return empty?


A:

As you already know, the file was truncated. That's why you can't read any more data from it.
But the mmap object still refers to the file, so it's very unlikely that the OS will free its memory.
In any case, the mmap object doesn't know that you truncated the file. It still thinks it's the whole file.
You can "unmap" the whole file with <code>m.close()</code> and then open a new mmap object with the new size.

