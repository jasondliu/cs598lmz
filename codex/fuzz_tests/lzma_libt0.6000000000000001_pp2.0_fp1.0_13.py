import lzma
lzma.LZMAError: Error -1 while decompressing data: invalid distance too far back
</code>
This is the code that I am using:
<code>import lzma

with lzma.open("C:\\Users\\rishabh\\Desktop\\test.txt.lzma", "rb") as fin:
    with open("C:\\Users\\rishabh\\Desktop\\test.txt", "wb") as fout:
        fout.write(fin.read())
</code>

