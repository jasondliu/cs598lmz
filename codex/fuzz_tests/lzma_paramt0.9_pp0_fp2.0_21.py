from lzma import LZMADecompressor
LZMADecompressor().decompress(header_str)
</code>
Even with the hackiest of hacks, I still can't get anything meaningful back.
Thanks in advance, I'm out of ideas.
edit: proper function code:
<code>def test():
    dirFile = "test/" + "headerfile.txt"
    isCompressed = False
    dest = open("test/test.e2fs", "wb+")
    with open(dirFile, "rb") as f:
        reader = f.read(1024)
        while reader:
            #decompress if compressed
            if (len(reader) == 1024 and isCompressed):
                #for some reason it's not working properly, the content is still compressed
                dec = LZMADecompressor().decompress(reader)
                dest.write(dec)

            else:
                dest.write(reader)
            reader = f.read(1024)


    dest.close()
</code>


A:

Edit
If I didn't misunderstand your code, the only possible problem, is that you're passing consecutive blocks of byte data to
