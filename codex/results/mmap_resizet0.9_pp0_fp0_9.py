import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(len(a))
    print(a)
</code>
which does not work quite as I expected - I get zero-length bytes as the result.
I'm not sure if it's just my usage of <code>mmap</code> (which is mysterious to me) or whether it's the <code>truncate()</code> that messes things up.
How do I truncate a file that's mapped with <code>mmap</code> and still expect to be able to read its original contents?


A:

You can't <code>truncate</code> some data and still expect to be able to read the original contents.
The <code>mmap</code> module documentation has this to say:
<blockquote>
<p>If one or more processes map a file in write mode, then both read and write references to the file may reflect the data changes made by either process. For example, if process A modifies part of a mapped file and then process B reads from the same region, process B may see the modifications that process A made. The reverse is also possible. The POSIX standard does not specify the order
