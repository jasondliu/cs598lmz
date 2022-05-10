import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a._ref_c=weakref.ref(a.c,callback)
keepalive.append(a)
gc.collect()
assert callback._alive_refs==0
del lst,callback,keepalive
print "bug"

"""
标准库中有一些用于支持引用计数的内建函数：getrefcount()。和weakref内建模块。
"""
lst=[]
d=weakref.WeakValueDictionary()
a=A()
d['primary']=a
lst.append(d)
a_wr=weakref.ref(a)
print a_wr,a_wr()
del a
print a_wr,a_wr()
print len(gc.get_referrers(a_wr))  #返回对弱引用对象活动引用的列表
d['primary']
