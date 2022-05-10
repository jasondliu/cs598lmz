import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
In the last line, I get the error:
<code>ValueError: cannot mmap an empty file
</code>
How can I avoid this error? I want to get the content of the file before truncation.


A:

You can't. 
You can't mmap an empty file. You can't even mmap a file that's just a single byte long, since the mmap module requires a length to be passed in, and it will throw an error if that length is greater than the file size.
You could, however, write a function that would read the contents of the file, truncate it, and then return the contents of the file.

