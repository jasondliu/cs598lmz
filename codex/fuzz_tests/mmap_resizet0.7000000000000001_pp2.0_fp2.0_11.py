import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
That gives the error <code>ValueError: mmap can't extend a read-only file</code>.
How can I get this to work?


A:

You can't get this to work, because the bytes you read are not the same bytes you wrote earlier.
Your file is zero bytes long. When you open it and ask for a mutable memory-mapped view of it, you get one that covers all of the file's contents. But, the file is zero bytes long, so the view you get maps to an empty byte array, which can't be resized.
But, even if the file were not empty, the view you get is not a view of the contents you wrote earlier; it's a view of the contents that are in the file now.
If you want to extend the file, you have to do it on the file object, not on the memory-mapped view.

