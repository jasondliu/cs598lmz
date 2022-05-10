import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m[0] = 1
    m.close()

with open('test', 'rb') as f:
    print(f.read(1))
</code>
I have no idea what I'm doing wrong here.
EDIT
Turns out, I just needed to call <code>m.flush()</code>


A:

You are not writing anything to the file.

<code>open</code> the file with <code>'w'</code> mode
<code>write</code> something
<code>open</code> the file with <code>'r+'</code> mode
<code>mmap</code> the file
<code>mmap</code>-write something
<code>mmap</code>-flush the map
<code>open</code> the file with <code>'r'</code> mode
<code>read</code> something

<code>import mmap

with open('test', 'w') as f:
    f.write("A")

with open('
