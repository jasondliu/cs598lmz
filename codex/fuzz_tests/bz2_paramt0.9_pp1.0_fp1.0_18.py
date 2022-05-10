from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# ############################
# # 先求均值，不能有None
print(mean( [1 ,2, 3, 4] ))
# ############################
# # 指定数据类型
# dtype
a = array([1,2,3],dtype=float)
print(a)
# dtype=float [1. 2. 3.]
a = array([1,2,3],dtype=complex)
print(a)
# ############################
# # 新建一个二维数组
b = array([[0,1,2],[
