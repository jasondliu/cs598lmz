import bz2
bz2.decompress('BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# 该程序的技巧在于调用decompress()方法，后面跟着一个字符串参数
# 这个参数包含了被压缩的数据
# 如果我们想处理一个包含很多存储在一个文件中被压缩的字符串，
# 或者通过网络
