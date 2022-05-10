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
# 例如，下面是一个缓存数据库连接的例子：

import weakref

class Database:
    def __init__(self):
        self.connections = weakref.WeakValueDictionary()

    def connect(self, db_name):
        if db_name not in self.connections:
            self.connections[db_name] = Connection(db
