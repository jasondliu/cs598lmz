import bz2
bz2.decompress("BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084")

# decompress the file inplace
with bz2.BZ2File('dickens.bz2', 'rb') as file:
    with open('dickens.txt', 'wb') as out:
        out.write(file.read())
 
# decompress the file and return uncompressed file-like object
with bz2.BZ2File('dickens.bz2', 'rb') as file:
    file.readline()
