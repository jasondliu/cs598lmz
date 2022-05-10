import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(2)
    m.close()
</code>
I have a similar program that does the same thing but opens the file with mode <code>'ab'</code>. I'd expect this to be equivalent, but it fails with an <code>OSError</code>. Is this a bug, or is there a reason why this doesn't work?
The reason I'm asking is that I'd like to use the <code>'ab'</code> mode for my program, but I'd rather not have to convert it to <code>'r+b'</code> just to resize the file.


A:

<code>OSError: [Errno 22] Invalid argument</code> is raised because <code>mmap</code> doesn't support <code>O_APPEND</code>.
<code>$ strace -eopen python mmap-test.py
...
open("test", O_WRONLY|O_CREAT|O_TRUNC, 0666) = 3
...
open("test", O_RDWR|O_APPEND)           = 3
...
open
