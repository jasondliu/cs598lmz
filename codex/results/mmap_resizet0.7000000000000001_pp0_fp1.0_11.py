import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()
</code>
<code>1</code> is printed as expected. But if you open the file in text mode using <code>'r+'</code>, it produces <code>b''</code> and an exception is raised:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: memory mapped size is zero
</code>
Thus, the question is why is the behavior different when the file is opened in text mode and how can I get the expected behavior without using <code>f.write</code> and without opening the file in binary mode?
I've tested the behavior on Linux and Windows.

