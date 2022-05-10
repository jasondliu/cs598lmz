import bz2
bz2.decompress(b)

# 使用bz2对压缩后的数据进行解压缩，就可以得到我们原始的数据：
# b'witch which has which witches wrist watch'
# 压缩后的数据可以保存到硬盘，或者通过网络传输。


# 小结
# 在Python中，字符串，二进制数据，整数等都是Sequence（序列）。通过for循环对一个序列进行迭代时，可以获得序列的每一个
