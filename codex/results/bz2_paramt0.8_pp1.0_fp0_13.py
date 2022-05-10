from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\
    c;\x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')
#b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc;\x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'

#开启上下文管理
with open('datafiles/somefile.txt', 'rt') as f:
    data = f.read()
#data files/somefile.txt
#with open('datafiles/somefile.txt', 'wt') as f:
#    f.write(data)
#with open('datafiles/somefile.txt', 'xt') as
