import bz2
bz2.decompress(bz2.compress(b'hello world'))

# 使用pickle模块将对象序列化到文件
import pickle
data = {'name': 'ACME', 'shares': 100, 'price': 542.23}
pickle.dumps(data)

# 将对象序列化到文件
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)

# 从文件中反序列化对象
with open('data.pkl', 'rb') as f:
    data = pickle.load(f)

# 使用json模块将对象序列化到文件
import json
json.dumps(data)

# 将对象序列化到文件

