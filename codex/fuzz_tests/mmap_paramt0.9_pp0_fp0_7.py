import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.resize(2 &lt;&lt; 20)    # Size must be &lt; limit in size_t.
    m.close()
</code>
To remove the file when you're done, use <code>os.unlink()</code>.
Here is a SO code snippet with more detail: https://stackoverflow.com/a/12772571/1399069

