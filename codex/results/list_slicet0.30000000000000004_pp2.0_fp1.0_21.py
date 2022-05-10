import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print(keepali0e)

#[<weakref at 0x7f6a5f6c8a68; to 'A' at 0x7f6a5f6c8a90>, []]

# 如果类定义了__slots__属性，它必须是一个字符串列表或元组，指明类实例允许有哪些属性。
# 如果定义了__slots__属性，Python将不会为该类的实例创建__dict__属性，这样可以节省内存。
# 如果定义了__slots__属性，Python将不允
