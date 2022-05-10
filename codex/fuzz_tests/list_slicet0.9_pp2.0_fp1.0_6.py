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
#print lst
#print keepali0e



"""
链表添加成员，列表长度动态膨胀，需要重新分配内存空间，如果在列表中元素又添加引用计数增加少于1的元素，干扰引用计数清零规则，绕过gc
其中的回收方式
"""
lst=[str()]
print 'lst type is %r'%type(lst)
lst2=lst[:]
lst2.append(lst2)
refcnt=sys.getrefcount(lst2)
print 'lst before append ref count is %d'%refcnt
