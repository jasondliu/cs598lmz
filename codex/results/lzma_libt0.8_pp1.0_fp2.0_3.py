import lzma
lzma.open()

def zipit(input,output):
    fs = open(input, 'rb')
    d = fs.read()
    fs.close()

    t = lzma.LZMACompressor()
    fs = open(output, 'wb')
    fs.write(t.compress(d))
    fs.close()
</code>


A:

Python3's <code>lzma</code> module doesn't have a <code>compress</code> function. Rather, you instantiate a new <code>LZMACompressor</code> object, then feed it the data to compress, like this:
<code>t = lzma.LZMACompressor()
fs = open(output, 'wb')
fs.write(t.compress(d))
fs.close()
</code>
See the docs for more details.

