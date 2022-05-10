import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
    m.close()
</code>
This code works fine on my machine, but it fails on the server with the following error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m[0] = b'\x00'
ValueError: cannot modify size of mapped region
</code>
I tried to find the difference between my machine and the server, but I can't find anything.
Both machines are running Ubuntu 16.04.
The server is a virtual machine running on a Windows 10 host.
I tried to run the code on a different virtual machine on the same host, and it worked fine.
I tried to run the code on a different virtual machine on a different host, and it failed.
I tried to run the code on a different virtual machine on a different host, but with a different Ubuntu version (14.04), and it worked fine.
I tried to run the code on a different virtual machine on a different host, but with a different Ubuntu version (14.04), and a different
