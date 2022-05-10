import bz2
bz2.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

b'pretty easy'

# BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084
# \b \a \t \n \f \r \v \xhh \' \" \\
# >>> 'hello'.encode('utf-8')
# b'hello'
# >>> b'hello'
# b'hello'

# It's important to use Unicode for all text because the world is full of different language encodings and Unicode’
