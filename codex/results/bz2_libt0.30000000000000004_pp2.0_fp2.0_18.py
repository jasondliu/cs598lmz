import bz2
bz2.decompress(bz2.compress(b'Hello World'))

import pickle
pickle.loads(pickle.dumps(dict(name='Bob', age=20, score=88)))

# 小结
# Python内置的pickle模块实现了基本的数据序列和反序列化。
# 通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
# 通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存
