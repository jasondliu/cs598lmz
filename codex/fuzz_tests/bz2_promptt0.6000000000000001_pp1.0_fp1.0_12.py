import bz2
# Test BZ2Decompressor
import io

data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'

with bz2.BZ2Decompressor() as dec:
    with io.BytesIO(data) as bio:
        for chunk in iter(lambda: bio.read(1), b''):
            print(repr(chunk), repr(dec.decompress(chunk)))

# Test BZ2File
with open('example.txt', 'rb') as input:
    with bz2.BZ2File('example.txt.bz2', 'wb') as output:
        output.writelines(input)

with bz2.BZ2File('example.txt.bz2', 'rb') as compressed:
    with open('example.txt.decompressed', 'wb')
