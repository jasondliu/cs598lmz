import bz2
bz2.decompress(bz2.compress(b'Hello World!'))

# 使用pickle存储对象
# pickle模块实现了基本的数据序列和反序列化，通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
# 通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
# 基本接口：
# pickle.dump(obj
