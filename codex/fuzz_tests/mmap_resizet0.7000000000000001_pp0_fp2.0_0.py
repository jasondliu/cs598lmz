import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
    print(a)
</code>
The problem is that I get:
<code>mmap.error: [Errno 22] Invalid argument
</code>
The stack trace is:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
  File "/usr/lib/python3.6/mmap.py", line 320, in __getitem__
    self._access(0)
  File "/usr/lib/python3.6/mmap.py", line 278, in _access
    os.read(self.fd, 1)
ValueError: read of closed file
</code>
If I don't truncate the file, everything works fine.
From the documentation I can't see anything that I'm doing wrong.
Is this a bug? What am I missing?
I'm running Python 3.6.3 on Debian.

