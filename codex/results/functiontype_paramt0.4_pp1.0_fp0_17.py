from types import FunctionType
list(FunctionType(lambda x: x*x, globals(), 'square'))

#
# 使用pickle模块将数据对象保存到文件
#
import pickle
d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()

#
# JSON
#
import json
d = dict(name='Bob', age=20, score=88)
json.dumps(d)

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str)

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s
