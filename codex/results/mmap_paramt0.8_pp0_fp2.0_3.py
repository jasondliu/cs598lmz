import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1)
    m.write(b'a')

assert open('test', 'rb').read() == b'a'
</code>
Works as expected. But if I make the file larger by adding a second byte...
<code>with open('test', 'wb') as f:
    f.write(bytes(2))
</code>
...it raises an exception:
<code>mmap.error: [Errno 22] Invalid argument
</code>
Is there a way to make this work, other than writing my own <code>memoryview</code>-based implementation?

