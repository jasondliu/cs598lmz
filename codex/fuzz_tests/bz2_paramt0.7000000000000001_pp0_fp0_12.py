from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(result)

# --------------------------
# 方法二：
import bz2
bz2.decompress(result)

# --------------------------
# 方法三：
result.decode('bz2_codec')

# 注意这里的result是一个bytes类型， 不能直接进行bz2解压
# 如果传入的是一个str类型的参数，那么返回的话也是一个bytes类型的结果
result = 'hello, world!'.encode('bz2_codec')
print(result)
# >>> b'BZh91AY&SY\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00
