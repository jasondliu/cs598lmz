import bz2
bz2.compress(open('C:/Users/Administrator/Desktop/图片.png','rb').read())
print('压缩参数未知，默认为9')
bz2.compress(open('C:/Users/Administrator/Desktop/图片.png','rb').read(),9)

print('==============================')
print('这个.compress 是静态方法，不用实例化')
print('解压缩')
B=bz2.BZ2File('C:/Users/Administrator/Desktop/diyi.bz2',rb')
B.read()
B.readlines()
