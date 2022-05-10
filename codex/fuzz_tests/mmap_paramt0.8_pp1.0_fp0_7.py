import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m[:] = bytes(2)
    m.flush()
    m.close()
</code>
If I try to open the file <code>test</code> with <code>hexedit</code>, I see that its content is <code>02</code> instead of <code>01</code>.
On the other hand, if I change <code>test</code> to <code>test.txt</code> (I don't know whether the extension of the file matters), I can see the file contains <code>01</code> when I open it with <code>hexedit</code>.
Does anyone know why I cannot edit the file <code>test</code> but succeed when I use a different extension?
I'm using Python 2.7.13 on Fedora 26.


A:

A hex editor doesn't work with text files because they contain binary data (carriage return + linefeed characters).

