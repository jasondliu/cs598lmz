import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:] = b'\0'
    m.close()
    f.close()

with open('test','rb') as f:
    print(f.read())
</code>
This prints out <code>b'\x00'</code>. This is different than the following, which prints <code>b'\x01'</code>:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:] = b'\0'
    f.close()
    m.close()

with open('test','rb') as f:
    print(f.read())
</code>
In both cases, the output file is <code>b'\x00'</code>, so it looks like the issue is in the way the OS buffers data back to the file. Does anyone know more about what is going on here?


A:

According to the docs
