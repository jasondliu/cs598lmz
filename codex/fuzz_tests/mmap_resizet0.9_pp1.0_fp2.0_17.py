import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print a
</code>
I think my question is also relevant to this previous question. However, I am not sure how to make use of the proposed solution -- keeping a copy of the file before truncating -- in a multithreaded environment.
What I want to achieve is to store some file pointer in a structure (which is not necessary to be thread safe), and use that structure in a mmap context in a separate thread. It seems that I cannot simply close the file after mmap'ing, but I need to keep the file descriptor around just in case I want to "reload" the mmap from that file.


A:

To expand on my previous comment. First, you could hold on to that <code>file</code> object everywhere else you need it. This is not efficient for a number of reasons. Even if it works, it's a hack.
A better way is to pass the file name around in your thread, and open it again if you need it. That way, you can open the file read-only if that is the mode you need.
Another way is to use John Machin's point about using (file, offset, size) instead of a pointer
