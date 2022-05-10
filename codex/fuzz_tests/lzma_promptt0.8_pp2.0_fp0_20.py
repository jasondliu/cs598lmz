import lzma
# Test LZMADecompressor

with open("file.txt", "rb") as inp:
    with lzma.open(inp, "rb") as lz_inp:
        with io.TextIOWrapper(lz_inp, encoding="utf-8") as text_inp:
            print(text_inp.read())
</code>
I don't know python so I don't know what the above code is doing. Outputting the file in binary, hexadecimal or any other output format would be ok.


A:

I have found the answer.
<code>s = b'x\x9c+\xce\xf1\x02\x00\x01\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x
