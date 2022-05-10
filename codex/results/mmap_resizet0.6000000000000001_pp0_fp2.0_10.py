import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # &lt;--- memory error
</code>
Here is the exception:
<code>Exception has occurred: MemoryError
memory allocation failed, allocating 2 bytes
  File "/usr/lib/python3.5/mmap.py", line 477, in __getitem__
  File "/usr/lib/python3.5/mmap.py", line 477, in __getitem__
  File "/usr/lib/python3.5/mmap.py", line 477, in __getitem__
  File "/usr/lib/python3.5/mmap.py", line 477, in __getitem__
  File "/usr/lib/python3.5/mmap.py", line 477, in __getitem__
  File "/usr/lib/python3.5/mmap.py", line 477, in __getitem__
  File "/usr/lib/python3.5/mmap.py", line 477, in __getitem__
  File "/usr/lib/python3.5/mmap.py", line 477, in __getitem__
  File "/
