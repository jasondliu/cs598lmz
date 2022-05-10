import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(1))
</code>
The output of <code>ls -l</code> is
<code>-rw-r--r--  1 user  staff  1B Nov  5 20:26 test
</code>
Why isn't the file size 1B?

