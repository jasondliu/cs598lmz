from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(response.data)

# 解压之后的内容
b'Welcome to pyspider!'
```

### 数据库操作

```python
# 创建数据库连接
import pymongo
client = pymongo.MongoClient('localhost', 27017)

# 创建数据库
db = client.test

# 创建数据表
table = db.students

# 插入数据
student = {'id': '20170101', 'name': 'Jordan', 'age': 20, 'gender': 'male'}
result = table.insert(student)
print(result)

# 查询数据
result = table.find_one({'name': 'Jordan'})
print(result)

# 更新数据
condition = {'name': '
