import bz2
# Test BZ2Decompressor

with open("bigdata.txt.bz2", "rb") as fp:
    dc = bz2.BZ2Decompressor()

    file_content = fp.read(100)
    print("Read 100 bytes from file")
    print("file_content:", file_content)

    print("decompressed_content:", dc.decompress(file_content))

print("File size:", os.path.getsize("bigdata.txt.bz2"))

print("Using file:", (100/os.path.getsize("bigdata.txt.bz2"))*100)
%timeit dc.decompress(file_content)

bz2.decompress(b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084")

with open
