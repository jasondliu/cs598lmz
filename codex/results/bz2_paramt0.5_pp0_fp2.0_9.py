from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open("test.bz2", "rb").read())

# 标准库中的 bz2 模块还包含一个 BZ2File 类，它可以像一个普通的文件对象一样工作，
# 但是它会自动的对读取的数据进行解压缩，并且在写入的时候会自动的进行压缩。
# 因此，你可以像下面这样读取一个压缩文件：

with BZ2File("test.bz2") as f:
    data = f.read()

# 同样的，
