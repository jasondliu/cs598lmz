import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    print(m[:1])
    m[0:1] = bytes([0])
    print(m[0:1])
</code>
I am on a Linux machine.


A:

I'm sure that some file systems will make a copy before modifying the value, but to me <code>-rw-rw-rw-</code> means that, at least for your test file, the system does not.
<blockquote>
<p>What about other file system drivers?</p>
</blockquote>
I don't think you can possibly answer this question. Python just calls the underlying operating system APIs, so Python is just as prone to copy values as any other application. Question 1 is: Does your OS provide mmap at all? Question 2 is: What do apps using the mmap() call do? If you find that Python is somehow different than other apps, then you can report it as a bug.

