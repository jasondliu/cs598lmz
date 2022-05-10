import bz2
bz2.decompress(bz2.compress(data))

# 使用pickle序列化对象
import pickle
pickled = pickle.dumps(data)
pickled

# 反序列化
data = pickle.loads(pickled)
data

# 将对象保存到文件中
f = open('somefile', 'wb')
pickle.dump(data, f)
f.close()

# 从文件中加载pickle数据
f = open('somefile', 'rb')
data = pickle.load(f)
f.close()

# pickle模块经常被用来在网络上传输数据，或者在磁盘上保存和读取数据
# 但是
