import bz2
bz2_file = bz2.BZ2File("test.bz2")
data = bz2_file.read()
bz2_file.close()
print(data)

# 如果想要更高效的读取，可以使用下面的方式
bz2_file = bz2.BZ2File("test.bz2")
for line in bz2_file:
    print(line)

# 如果想要写入，可以使用BZ2File对象的write()方法
bz2_file = bz2.BZ2File("test.bz2", "w")
bz2_file.write(b"Hello World!")
bz2_file.close()
