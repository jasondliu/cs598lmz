import bz2
bz2.decompress(bz2.compress(b'Hello'))

# 使用pickle模块将对象序列化为字节流
import pickle
d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)

# 反序列化
d = pickle.loads(pickle.dumps(d))

# 将对象序列化后写入文件
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

# 从文件中反序列化出对象
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()

# 将对象序列化为JSON
import json
d = dict(name='Bob', age=20, score
