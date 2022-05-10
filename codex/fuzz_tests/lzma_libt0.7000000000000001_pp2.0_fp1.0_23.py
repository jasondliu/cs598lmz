import lzma
lzma.decompress(f.read())
</code>
This will decompress the lzma file and print the decompressed data to stdout.
To write to a file, use the <code>write</code> command:
<code>f = open('compressed.lzma')
import lzma
lzma.decompress(f.read()).write('decompressed.txt')
</code>

