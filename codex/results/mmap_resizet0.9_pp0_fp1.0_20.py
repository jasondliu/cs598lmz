import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    a = 'abcd'
    m[:] = a
</code>
I expected the <code>mmap</code> object to still be usable after <code>f.truncate()</code>, but I got <code>ValueError: mmap offset is greater than file size</code> error.
So this raises two questions:

How do I access the old data if I have to truncate the file?
How do I access data after a file is truncated?



A:

I'll tell you up front that the answer you'll hear from most experts here is that you should not use <code>mmap</code> for anything except binary files, or if you have a C program that writes binary files for consumption by a Python program. Your best bet is to just read and write the file normally, with normal file objects.
But if you insist, you can get the behavior you want from mmap by creating the mmap object after you've done a <code>f.truncate()</code> and then opening the file in a separate file object, writing that data to the mmap object and then closing the file object so that the size
