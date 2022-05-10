import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
and a similar error on windows:
<code>Traceback (most recent call last):
  File "tmp", line 10, in &lt;module&gt;
    a = m[:]
OSError: [WinError 299] Only part of a ReadProcessMemory or WriteProcessMemory request was completed
</code>
In order to fix this behaviour, I need to explicitly unmap the memory. If I do not, I can access the memory as long as I do not close the file. However after closing the file and re-opening it the mmap length is zero. 
In other words, this is the minimal code with which I do not have the error:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno
