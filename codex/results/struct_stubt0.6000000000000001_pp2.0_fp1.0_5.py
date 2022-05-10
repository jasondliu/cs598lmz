from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<h')
s.pack(1)

# 仅当使用类或者实例的时候，才会调用__getattr__
class Test:
    def __getattribute__(self, item):
        print("__getattribute__", item)
        return super().__getattribute__(item)

    def __getattr__(self, item):
        print("__getattr__", item)
        return super().__getattr__(item)

    def __setattr__(self, key, value):
        print("__setattr__", key, value)
        super().__setattr__(key, value)

t = Test()
t.a = 1
t.a
t.a
t.b
t.b
t.b
