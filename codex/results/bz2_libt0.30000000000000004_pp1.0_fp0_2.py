import bz2
bz2.decompress(bz2.compress(b"hello world"))

# 字符串格式化
print("%s %s" % ("hello", "world"))
print("{} {}".format("hello", "world"))
print("{0} {1}".format("hello", "world"))
print("{1} {0}".format("hello", "world"))
print("{0} {0}".format("hello", "world"))
print("{1} {0}".format("hello", "world"))

# 字符串格式化
print("{hello} {world}".format(hello="hello", world="world"))
print("{0[0]} {0[1]}".format(["hello", "world"]))
print("{0[hello]} {0[world]}".format({'hello': 'hello', 'world': 'world'}))
print("{0[hello]} {0[world]}".format(dict(hello="hello", world="world")))

# 字
