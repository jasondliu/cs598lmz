import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0,
                  access=mmap.ACCESS_WRITE)  # default value of access is ACCESS_WRITE
    m[0] = b'2'
    m.close()

with open('test', 'rb') as f:
    print(f.read())  # b'2'
</code>
When I tried to run above code by python3.6, it will cause a <code>ValueError</code> exception.
<code>Traceback (most recent call last):
  File "test.py", line 6, in &lt;module&gt;
    access=mmap.ACCESS_WRITE) # default value of access is ACCESS_WRITE
  File "/usr/lib/python3.6/mmap.py", line 284, in __init__
    _map_file(fileno, length, flags, prot, access, offset)
ValueError: mmap length is greater than file size
</code>
I search the source code of python3.6's mmap.py and find the source of error.
<code>if length &gt; file_size:
