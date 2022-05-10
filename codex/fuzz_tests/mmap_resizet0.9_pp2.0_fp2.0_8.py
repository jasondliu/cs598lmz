import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
When running this program, I am receiving error:
<code>Exception has occurred: mmap.error
[Errno 28] No space left on device
  File "&lt;stdin&gt;", line 3, in &lt;module&gt;
</code>
Why there is no space on the device and how should I handle the situation if I would like to have the contents of the memory map 'a' after truncation?
I have found some discussion on the topic (example: https://mail.python.org/pipermail/python-list/2009-April/542398.html) but I am still not understanding.


A:

<blockquote>
<p>Why there is no space on the device and how should I handle the situation if I would like to have the contents of the memory map 'a' after truncation?</p>
</blockquote>
Python uses the operating system to manage mmap files and the OS does not free the space (you can think of the OS as not being aware of the truncation, because it is from Python), so there are no memory space left. 
If you
