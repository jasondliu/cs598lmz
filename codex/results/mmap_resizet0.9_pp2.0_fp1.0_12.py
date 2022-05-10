import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # this is in the non-existing memory and Python crashes.
    print(a)
</code>
I've faced this problem in production, where real file truncate happened while I was making an mmap copy. This is a showstopper and I'm unable to solve it. Rename+copy is not possible, because it doesn't guarantee that file won't be deleted.


A:

You shouldn't use mmap in this case.  The simplest way would be to open two files: the current and the new.  Then you can read bytes from the former and write them to the latter.  After that, rename the new file over the old one.  You seem to say that you can't do that, but there really isn't any reason why not.
The only other possibility is to write something from scratch.  This would entail mapping the file yourself, without relying on the OS's filesystem.  Then you have full flexibility to extend the file when you need to.

