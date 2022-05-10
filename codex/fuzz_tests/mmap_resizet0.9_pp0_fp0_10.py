import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(len(a))
</code>
This code crashes with <code>ValueError: cannot mmap an empty file</code>.
Please tell me that it's not just my machine that's wonky.


A:

This is documented behaviour. The idea is that if you mmap in the first place, you probably want it to keep working, even if the file gets truncated. From the exception you see that Python does indeed let you truncate the file, but then raises an exception to be clear that the mmap is no longer valid. If it let you keep using the <code>mmap</code> in this situation, then the behaviour of your code would depend on the underlying operating system in the tricky case where a file is extended without going through <code>mmap</code>. Imagine a file that is mmapped into address <code>0..10</code>; if it's extended, the extension might end up somewhere else, or it might end up at <code>10</code>. 
You can solve this in Python 3.3 by first mapping a file, then extending it to exactly the same size, then truncating it. Since <code>mmap</
