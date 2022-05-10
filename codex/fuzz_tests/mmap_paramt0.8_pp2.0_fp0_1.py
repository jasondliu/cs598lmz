import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = ord('1')
    m.flush()
    m.close()
</code>


A:

You are missing a flush call to make the change visible to other processes:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = ord('1')
    m.flush()  # need flush here
    m.close()
</code>

