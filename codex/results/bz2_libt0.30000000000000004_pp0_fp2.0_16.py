import bz2
bz2.decompress(bz2.compress(b'hello world'))

# 另一个例子是，接受一个任意大小的输入，并且按照行分析输出，假设内容如下：
#
# hello world
# this is
# a test
# 如果是一个普通的文件，可以直接使用for循环来读取：
#
# with open('/path/to/data.txt', 'r') as f:
#     for line in f:
#         print(line)
# 但如果是一个非常大的文件，内存占用会很大，而且效
