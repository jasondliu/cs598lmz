import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)
</code>
The output is <code>b'\x00'</code>, which means that the <code>mmap</code> object was not notified that the file was truncated.
If I change the mode to <code>'a+'</code>, it works fine.
I have also tried <code>m.resize(0)</code> and <code>m.resize(0, 0)</code> instead of <code>f.truncate()</code> with the same result.
Is this a bug, or is the correct behaviour?
I'm using Python 3.5.1.


A:

I got an answer on the Python bug tracker. This is the correct behaviour.

