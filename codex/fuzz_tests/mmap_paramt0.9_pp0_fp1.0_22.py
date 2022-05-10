import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0) 
</code>
If I omit <code>0</code> parameter then the call succeeds. I understand the error message, but can't spot the mistake in the parameters. What is the correct way to create a <code>mmap.mmap</code> on a file that already exists?


A:

You don't need to use the file size; the second argument can be 0. The following works for me:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
</code>

