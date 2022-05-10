import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 100)
    print m.size()
</code>
gives
<code>1
</code>
Is there any way to get <code>mmap.mmap</code> to create a new file of size <code>size</code> if the file doesn't exist?
Or is there any other <code>mmap</code> function that allows creating a new file of size <code>size</code> if the file doesn't exist?


A:

<code>mmap</code> just lets you access files as binary, rather than using system calls. Your example creates and opens a file, so you're using <code>mmap</code> correctly. If you remove the <code>1</code> and add an if condition:
<code>with open('test', 'wb') as f:
    if os.path.exists('test'):
        f.write(bytes(1))
    else:
        f.write(bytes(100))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 100)
    print m
