import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code works as expected on Linux, but on Windows it raises an exception:
<code>Traceback (most recent call last):
  File "C:\Users\user\Desktop\test.py", line 10, in &lt;module&gt;
    a = m[:]
WindowsError: [Error 87] The parameter is incorrect
</code>
What is the reason of this behavior?

