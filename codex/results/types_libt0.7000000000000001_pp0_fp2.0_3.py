import types
types.MethodType(run, D(), D)

# ok
# D.__dict__['run'].__get__(D(), D)()
# D().run()
D().run

# -----------------------------------------------------------------------------
# __get__, __getattr__, __getattribute__

# 通过__getattr__获取不存在的属性，会触发调用
# 通过__getattribute__获取不存在的属性，不会触发调用
class D:
    def __getattr__(self, item):
        print('D.__getattr__')

    def __getattribute__(self, item):
        print('D.__getattribute__')


d = D()
print(d.k)
# print(d.__dict__)

# -----------------------------------------------------------------------------
# __getattribute__, __getattr__

# __getattr__, __getattribute__的优先
