import lzma
# Test LZMADecompressor

print lzma.LZMADecompressor().decompress(open(sys.argv[1], 'rb').read())
</code>
and run it on the command line as:
<code>$ python testlzma.py ./SRC/file1.bz2
</code>
it works, outputting the content of <code>file1.bz2</code>. However, when I change the <code>open</code> line to <code>open(sys.argv[1], 'rb', buffering=0)</code> I get the following error:
<code>Traceback (most recent call last):
  File "testlzma.py", line 10, in &lt;module&gt;
    print lzma.LZMADecompressor().decompress(open(sys.argv[1], 'rb', buffering=0).read())
  File "/usr/lib/python2.7/lzma.py", line 227, in decompress
    return self.decompressobj.decompress(data)
error: Error -
