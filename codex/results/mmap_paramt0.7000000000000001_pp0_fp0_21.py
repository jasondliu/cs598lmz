import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:] = b'\x00'
    m.close()
</code>
but this is not working on Android.
<code>Traceback (most recent call last):
  File "/data/data/com.termux/files/usr/lib/python3.8/mmap.py", line 1240, in __init__
    _mmap.mmap(self, fileno, length, flags, prot, access, offset)
OSError: [Errno 22] Invalid argument

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/data/data/com.termux/files/home/test.py", line 6, in &lt;module&gt;
    m = mmap.mmap(f.fileno(), 0)
  File "/data/data/com.termux/files/usr/lib/python3.8/mmap.py", line 1242, in __init__
    raise OSError(err, strerror(err))
OSError: [Errno 22] Invalid
