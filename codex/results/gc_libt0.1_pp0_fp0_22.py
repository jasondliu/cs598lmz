import gc, weakref

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print(d['primary'])
del a
gc.collect()
print(d['primary'])

# 10
# 10

# 弱引用字典的一个主要用途是实现缓存。
# 例如，下面是一个缓存数据库查询结果的类：

import time
import sqlite3

class Query(object):
    def __init__(self, query):
        self.query = query
        self.creation_time = time.time()

    def __call__(self):
        fetch_data()
        return self.query

