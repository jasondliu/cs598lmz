from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xf6\xff') 
# b'hello'
</code>
The code I am using is,
<code>import sys
import lzma

infile = sys.argv[1]
outfile = sys.argv[2]

with lzma.open(infile) as fin:
    with open(outfile, 'wb') as fout:
        while True:
            buf = fin.read(1024000)
            if not buf:
                break
            fout.write(buf)
</code>
What am I doing wrong?

