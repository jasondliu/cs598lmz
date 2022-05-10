import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(type(a))
    print(a)
</code>
It throws the error:
<code>Traceback (most recent call last):
  File "mmap-test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: cannot mmap an empty file
</code>
What is the correct/best way to mmap an empty file?


A:

According to this bug report, it should work, at least in Linux and OSX. You might want to open an issue on the issue tracker, or reference the existing issue.

