import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # error: mmap closed or invalid

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(10)
    m[9] = '1'.encode('utf8')
</code>
gives:
<code>Traceback (most recent call last):
  File "/home/dmitry/work/projects/trade/trade/tests/test_simulate_operator.py", line 29, in &lt;module&gt;
    a = m[:] # error: mmap closed or invalid
ValueError: mmap closed or invalid
</code>
It seems that <code>mmap</code> object is unaware of truncate operation on file. Can I somehow make it aware of it?
Python 3.4, linux
remarks:

I know about <code>mmap.resize</code> in <code>mmap</code> library. However writing to <code>mmap</code> object after resizing produces message <code>ValueError: cannot resize an mmap backed by a file</
