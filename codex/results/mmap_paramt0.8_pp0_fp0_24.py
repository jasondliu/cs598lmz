import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(5)
    m.flush()
    print(m[0])
    m.close()

</code>
The output is <code>b'\x05'</code>. 
Is it a common practice to do file I/O in that way?


A:

It's not a good practice at all, because you can't "teach" the operating system (and your editor too!!) that your file has been modified, since the operating system keeps track of the file size and modification time and many other parameters by default (and it's not a good practice to mess with them, believe me!)
<code>mmap</code> is commonly used in Python when you have a very big file and you want to access it randomly, but you don't want to load the whole file into memory.
EDIT:
Also note that <code>bytes(5)</code> is incorrect. It is the same as <code>bytes(1) * 5</code>, and it gives you a 5-element tuple of <code>bytes(1)</code>, which is <code>b'\x01'</code
