import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(200)

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(200)
</code>
Running this code on a linux machine gives the following error:
<code>Traceback (most recent call last):
  File "test.py", line 14, in &lt;module&gt;
    m.resize(200)
mmap.error: [Errno 22] Invalid argument
</code>
What am I doing wrong?


A:

The <code>mmap</code> module allows you to map a file into memory, and then access it as if it were just a regular Python array. However, you can't make the underlying file bigger or smaller using the <code>mmap</code> module.
The reason is that <code>mmap</code> is a thin wrapper around the OS's memory mapping functionality. If you want to change the size of the file, you have to use the <code>os</code> module to do that.
I think what you
