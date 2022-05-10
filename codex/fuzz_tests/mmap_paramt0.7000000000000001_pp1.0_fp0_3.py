import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
</code>
This brings an IOError:
<code>Traceback (most recent call last):
  File "test.py", line 11, in &lt;module&gt;
    m.write(bytes(2))
IOError: [Errno 28] No space left on device
</code>
Am I doing something wrong?
Edit:
It's a Raspberry Pi running Raspbian.  Here's the output of <code>df -h</code>:
<code>Filesystem      Size  Used Avail Use% Mounted on
/dev/root        14G   14G     0 100% /
devtmpfs        485M     0  485M   0% /dev
tmpfs           493M     0  493M   0% /dev/shm
tmpfs           493M  1.5M  491M   1% /run
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
tmpfs           493M     0  493M   0% /
