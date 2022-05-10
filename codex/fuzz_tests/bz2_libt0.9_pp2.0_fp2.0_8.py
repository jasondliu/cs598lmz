import bz2
bz2.decompress(data)

# exec() and eval()
# eval是执行某个字符串形式的表达式
exec("import os",globals(),globals())
os
# eval解析其参数，看作一个python表达式，然后计算结果，并返回结果
eval("1 + 2 + 3")

# 文件对象和sys.stdout
# 我们都知道print()函数会将我们想要打印的内容显示在终端上，那么sys.stdout就是这个打印print函数的默认值
# 我
