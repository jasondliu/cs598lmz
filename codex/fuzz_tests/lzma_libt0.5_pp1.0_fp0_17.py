import lzma
lzma.open(file, mode='r', encoding=None, errors=None, newline=None)
</code>
So, I am looking for a way to open the file and read it as a string. 
Any help would be appreciated.


A:

You should be able to open the file and read it as a string.
<code>import lzma
with lzma.open(file) as f:
    data = f.read()
</code>

