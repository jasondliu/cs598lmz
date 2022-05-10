import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:] = bytes([1])

    # This can be read by any other process
    with open('/dev/shm/test_mmap_copy', 'wb') as f2:
        f2.write(m)

    # This can't
    with open('test_mmap_copy', 'wb') as f2:
        f2.write(m)
</code>
The first write succeeds. The second write fails:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 2, in &lt;module&gt;
OSError: [Errno 22] Invalid argument
</code>

