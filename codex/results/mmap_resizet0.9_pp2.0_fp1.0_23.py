import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Output - <code>UnicodeDecodeError: 'utf-8' codec can't decode byte 0x01 in position 0: invalid start byte</code>
Why does truncation affects mmap object?
P.S. I know what exactly going on if I do <code>a = m[0]</code> and I will never use mmap this way, but I'm still curious why truncation throws an exception.

P.P.S. Here is the code with just open() and truncate() that seems to work well -
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    f.truncate()
    a = f.read()
</code>


A:

To elaborate on @skipper-ca's answer, basically that mmap object keeps a reference to the object it was initialized with, which is the file object in your case. And when you truncate that file object, the mmap object won't do anything about it and still behaves as if the original content is there.
