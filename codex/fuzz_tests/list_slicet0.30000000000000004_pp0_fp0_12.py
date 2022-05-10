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

#这个程序会报错，因为在删除a的时候，a.c引用了a，所以a不能被删除，而在callback函数中，del lst[0]会调用__delitem__方法，
# 在__delitem__方法中，会调用__getitem__方法，在__getitem__方法中，会调用__len__方法，在__len__方法中，会调用__getitem__方法，
# 在__getitem__方法中，会调用__len__方法，在__len__方法中，
