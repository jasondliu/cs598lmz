import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
The last line will give the error:
<code>Traceback (most recent call last):
  File "C:/Users/Jeppe/Desktop/test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: cannot mmap an empty file
</code>
It is because the file is empty when trying to read the mmap.
Is there a simple way to fix this, so one could use mmap on a file that might be empty?


A:

I tried to reproduce the problem, but it seems to work.
<code>with open('test', 'w') as f:
    f.write('')

with open('test', 'r+') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
When I run it, I get an empty <code>a</code>.
If I run it again, I get an empty <code>a</code> and the
