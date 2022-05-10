import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I want to test code that has this line (second-to-last line of above code) in it.
I want to test it in such a way that it doesn't call <code>truncate()</code> to actually delete the file, because I want to leave it in unit testing.
Is there a way to apply a conditional so that if <code>test</code> is the filename being truncated, don't do it?

