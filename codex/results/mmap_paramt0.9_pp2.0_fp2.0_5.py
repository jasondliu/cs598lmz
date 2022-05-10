import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 2
    m.close()

# This works on Linux, but not Windows:
#   TypeError: must be read-write buffer, not mmap

open('test').read()
</code>


A:

You may do it using <code>open()</code>'s <code>buffer</code> feature. On Windows, use win32file.SetFilePointerEx to reach the header:
<code>with open('test', 'r+b') as f:
    win32file.SetFilePointerEx(f.fileno(), 0, 0)
    m=mmap.mmap(f.fileno(), 0,access=mmap.ACCESS_WRITE)
    print(m[0])
    m[0]=2
    print(m[0])
    m.flush()
    m.close()
</code>
Output:
<code>1
2
</code>

