from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
</code>
but it gives me
<blockquote>
<p>b'\xdf\xff\xff\xff\x1e' is not a multiple of the block size</p>
</blockquote>


A:

lzma is most likely not what you need. It is a very specific compression tool and format. I would suggest you install lzop and run it on your file.
<code>$ lzop -d myfile.lzo
</code>
This will decompress the file and output it on the standard output. If you want to output it to a file, you can use -o flag.
<code>$ lzop -d myfile.lzo -o myfile
</code>

