import weakref


class MyClass:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "MyClass(%r)" % self.name


c = MyClass("A")
c_id = id(c)
d = weakref.ref(c)
print(d)
print(d())
print(d() is c)
print(d() is None)

"""
weakref.ref(object_name) 表示创建一个弱引用对象
弱引用对象不可以自己访问被引用的对象，必须跟一个字典绑定在一起，
以此满足当字典中有Key，value是一个对象被释放之
