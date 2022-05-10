import bz2
# Test BZ2Decompressor for output
decompressor = bz2.BZ2Decompressor()
with open('D:\python\wiki.xml.bz2', mode='rb') as input:
    with open('D:\python\wiki.xml', mode='wb') as output:
        for block in iter(lambda : input.read(1024 * 1024), b''):
            output.write(decompressor.decompress(block))
 
import codecs
# Test stream reader
input = bz2.BZ2File('D:\python\wiki.xml.bz2')
output = codecs.open('D:\python\wiki.xml', mode='w', encoding='utf-8')
for line in input:
    output.write(line.decode('utf-8'))
input.close()
output.close()
 
# Test stream writer
input = codecs.open('D:\python\wiki.xml', mode='r', encoding='utf-8')
output = bz2.BZ2File('D:\python\wiki.xml.bz2', mode='wb')
for line in input
