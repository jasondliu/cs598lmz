import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 0
    m.close()
</code>
But this is not working for me. I am getting this error:
<code>Traceback (most recent call last):
  File "test.py", line 7, in &lt;module&gt;
    m[0] = 0
TypeError: 'mmap.mmap' object does not support item assignment
</code>
I am not sure what is wrong. I am using Python 3.6.


A:

You are using the wrong mode. The <code>mmap</code> module uses the same mode strings as the <code>open()</code> function, and you need to use <code>r+</code> to be able to modify the file.
The <code>b</code> mode is optional, and you should only use it if you need to explicitly use bytes objects.

