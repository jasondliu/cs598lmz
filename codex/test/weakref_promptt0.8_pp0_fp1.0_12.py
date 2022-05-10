import weakref
# Test weakref.ref()
# 创建一个弱引用对象
wr = weakref.ref(object())
print(wr)
# 获取对象
wr_object = wr()
print(wr_object)
# 清除对象
del wr_object
print(wr())

# Test weakref.getweakrefcount()
x = list()
y = x
z = x
print(str(weakref.getweakrefcount(x)) + ' references to x')
# Test weakref.getweakrefs()
refs = weakref.getweakrefs(x)
for ref in refs:
    print(ref)
# Test weakref.WeakKeyDictionary
# 弱键字典
d = weakref.WeakKeyDictionary()
d['Foo'] = 1
d['Bar'] = 2
# 打印字典
print(d)
print(d['Foo'])
print(d['Bar'])
#
