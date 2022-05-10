import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
gc.collect()
lst[0]='a'
lst.append(lst)
lst.append(weakref.ref(lst,callback))
del lst
gc.collect()
print keepalive[0].c

#结果：
#<__main__.A object at 0x7f8c8e2d1f10>

#结论：
#虽然执行了del lst[0]，但是因为lst[0]还存在引用，所以不会被回收。
#为什么lst[0]还存在引用？因为lst[0]是str类型，str类型是不可变的，所以lst[0]的值
