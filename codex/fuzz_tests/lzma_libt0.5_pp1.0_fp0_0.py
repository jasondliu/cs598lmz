import lzma
lzma.decompress(data)
</code>
I tried to write the data to a file and decompress it using the <code>xz</code> command line tool and it worked.
I'm using Python 3.5.2 on Ubuntu 16.04.


A:

You can use the <code>lzma</code> module from the <code>backports.lzma</code> package:
<code>pip install backports.lzma
</code>
Then, use the module like this:
<code>from backports import lzma

with open('myfile', 'rb') as f:
    data = f.read()

lzma.decompress(data)
</code>

