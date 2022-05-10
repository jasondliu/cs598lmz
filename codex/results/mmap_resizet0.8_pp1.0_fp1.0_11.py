import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This still throws a <code>ValueError: mmap offset is greater than file size</code> and, I believe, rightly so. However, this is the question: Is this behavior guaranteed? 
In other words, is it guaranteed that the file will not be truncated until it is closed? I am writing some code that depends on this behavior, but I would like to make sure it will not fail in the future.


A:

<blockquote>
<p>Is this behavior guaranteed?</p>
</blockquote>
Yes, but only because the behavior is "if you truncate a <code>mmap</code>ed file, you get a <code>ValueError</code>" - that is a specific behavior of <code>mmap</code>, and you get it because the file is <code>mmap</code>ed.
As for "is it guaranteed that the file will not be truncated until it is closed", no, that's not guaranteed either. The <code>truncate</code> method itself is designed to do what you want, as long as you pass it the correct argument to truncate it to the current location
