import weakref
# Test weakref.ref
# weakref.ref 常用， 通过弱引用到对象的方式来获取对象， 防止对象无法收回导致内存泄露。
# 注意， 使用 weakref.ref 之后， 对象将在垃圾回收时被彻底释放， 可以通过 weakref.ref 来判断对象是否被释放。


class Obj(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Obj name: {}'.format(self.name)


# 直接引用
obj = Obj('python')

