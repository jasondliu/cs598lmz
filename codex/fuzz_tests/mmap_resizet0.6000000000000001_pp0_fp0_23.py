import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I'm getting this error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I'm using python 3.6.3.
I thought that mmap has to be synced with file after truncate.
What is the right way to do it?


A:

I'm not sure if I'm getting your question right, but if you want to truncate a file and then get the new contents of the truncated file, you can do it like this:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(0)
    m.write(b'a')
    f.seek(0)
    a = f.read()
    m
