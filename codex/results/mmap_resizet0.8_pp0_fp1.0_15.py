import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I have read that with <code>mmap</code> the file content is loaded into memory when it is created. So I think this should work. But <code>a</code> is always empty.
When I run the above code and then open the file in an editor, I can see that the content is still there.
Why can't I access it?


A:

I found the solution to my problem - using <code>mmap.ACCESS_READ</code> instead of <code>mmap.ACCESS_DEFAULT</code> solves the issue.

