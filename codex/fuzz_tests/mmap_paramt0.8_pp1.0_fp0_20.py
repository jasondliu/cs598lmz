import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write_byte(b'a')
    m.seek(0)
    m.write_byte(bytes([1]))
</code>
I am getting the following error:
<code>Traceback (most recent call last):
  File "/usr/local/Cellar/python/2.7.10/Frameworks/Python.framework/Versions/2.7/lib/python2.7/mmap.py", line 259, in write
    self._verify_mmap()
  File "/usr/local/Cellar/python/2.7.10/Frameworks/Python.framework/Versions/2.7/lib/python2.7/mmap.py", line 89, in _verify_mmap
    raise ValueError("mmap closed or invalid")
ValueError: mmap closed or invalid

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m.write_byte(bytes([1]))
  File "/usr/local/
