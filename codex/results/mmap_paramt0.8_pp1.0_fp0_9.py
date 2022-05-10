import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 0x11
    m.close()

with open('test', 'r') as f:
    print(f.read())
</code>
There are only two logical output:

the file is corrupted (only the first byte is changed), but the file size is still 1 byte
the file is corruptly changed (the first byte is changed, and the file size becomes 44 bytes, so some non-sense bytes are appended to the file)

I've tested it on Python 3.5 and 3.8, on MacOS 10.14 and 10.15, on VSCode 1.45 and 1.47, using both the integrated terminal and iTerm 2.  I've also tried spawning a new shell.
I'm pretty new to programming, but I believe it's either a bug or a feature of Python 3, or an implementation detail of mmap.
I've tried the same code on Python 2, and it doesn't have this problem.
Does someone know why this happen?  Thanks!


A:

<code>bytes(1)</code> is not a valid file.  It is the byte <code
