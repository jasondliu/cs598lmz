import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The code above will result in a <code>ValueError</code>:
<code>ValueError: mmap offset is greater than file size
</code>
If I do not use <code>truncate</code> then the code works fine. I know that one solution is to use <code>mmap.resize</code> but it is not available in windows and I cannot use it.
So my question is -- what am I doing wrong? If I use <code>truncate</code>, then and close the file, then open it again and use <code>mmap</code>, then the code works fine.


A:

I guess you're using windows, so I did the same.
Do not use your code. I've done some research, and it seems that on windows, you can't use truncate after mmap
Here is some code I've come up with. (didn't test it on Linux)
<code>import mmap

with open('test', 'wb') as f:
    f.write(b'\0')

with open('test', 'r+
