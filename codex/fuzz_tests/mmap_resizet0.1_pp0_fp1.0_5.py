import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I am using Python 3.6.1 on Windows 10.
I am trying to understand how mmap works. I want to be able to read the file after truncating it. I know that I can use <code>m.resize(0)</code> to resize the mmap object, but I want to understand why I get the error.
I have read the documentation and I understand that the mmap object is a view of the file. I also understand that the file is truncated, but I don't understand why the mmap object is not updated.
I have also tried to use <code>m.resize(0)</code> before truncating the file, but I get the same error.
I have also tried to use <code>m.close()</code> before truncating the file, but I get the same error.
I have also tried
