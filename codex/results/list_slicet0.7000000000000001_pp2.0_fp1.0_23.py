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
print keepali0e

#列表和字典的区别

#a[key]=value速度慢；用内置函数xrange(n)
#可以通过索引访问列表，可以通过键访问字典
#列表中存放的元素可以改变，字典中的元素不能改变
#列表中的元素没有顺序，在字典中，元素是有顺序的
#列表中的元素是可以重复的，字典中的元素不能重复
#列表
