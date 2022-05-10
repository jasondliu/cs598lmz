from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x5dm\x4dZ\x01\x00\x00\x00\x04\x00\x02\x00!\x01\x00 \x01\x00\x02\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

print(1)
#维基百科点击流数据：
#https://dumps.wikimedia.org/other/pagecounts-raw/
#文件格式：
#<project code>.<date-time>.<page type>.<compression>.gz
#存放数据的文件如下：
#https://dumps.wikimedia.org/other/pagecounts-raw/2010/2010-03/pagecounts-20100329-000000.gz
#https://d
