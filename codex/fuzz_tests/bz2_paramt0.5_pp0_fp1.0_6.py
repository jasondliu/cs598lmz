from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'\x42\x5a\x68\x39\x31\x41\x59\x26\x53\x59')

# 如果你有一个包含了大量小字符串的字节序列，并且你想将它们合并成一个大的字符串，
# 那么你可以使用 io.StringIO() 来简化这个操作。比如，下面的代码创建了一个包含了三个小字符串的列表：
data = ['Hello world!\n', '\n', 'Goodbye world!\n']

# 然后你可以像下面
