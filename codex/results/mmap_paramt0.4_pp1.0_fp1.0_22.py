import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(2)
    m.write(bytes(1))
    m.close()
</code>
The above code works fine on Windows but returns an error on Linux:
<code>mmap.error: [Errno 22] Invalid argument
</code>
I tried to find the reason for this error but couldn't find anything. Does anyone know what causes this error and how to fix it?

