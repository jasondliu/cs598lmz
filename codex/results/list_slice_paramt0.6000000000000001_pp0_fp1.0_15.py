import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
keepali0e.append(weakref.ref(lst[0],callback))
lst.append(str())
print(lst)

#结果：
#['']
#此处，首先是创建了lst这个列表，在列表中插入了一个空字符串；
#然后是创建了a这个对象，并将a的引用指向本身，即a.c=a；
#然后是将a的弱引用添加到keepali0e列表中，并且添加了回调函数，这个回调函数的
