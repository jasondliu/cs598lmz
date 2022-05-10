import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1)
    m[0] = bytes(255)

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1)
    print(m[0])
</code>
This example, as far as I can tell, should write a single byte of value 1 to a file called "test", then it should open the file and overwrite only the first byte with a byte of value 255, and then it should print out the byte and get 255. 
The problem is, the output is always 1. I'm using Python 2 and Windows, if that matters. 
Does the fact that I'm using <code>map.mmap</code> and not <code>ctypes</code> or something else matter here? What am I doing wrong?


A:

You're overwriting the one byte (1) with a two-byte string (b'\x00\xff') -- that single byte gets overwritten, but the second byte in that buffer extends to the end of the buffer and beyond.
Writing 255 to the first location should look like this:
<code>m[0:
