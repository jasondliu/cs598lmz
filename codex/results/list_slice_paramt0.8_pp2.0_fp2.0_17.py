import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)

'''
要强调的是，弱引用不能独立存在，还是要和一个强引用绑定在一起，当原有的强引用被彻底释放，那么弱引用也会被释放掉，
在这里，被释放的弱引用调用的回调函数是callback，这个回调函数指定删除了lst的第一个元素，那么执行print时，能看到lst的
第一
