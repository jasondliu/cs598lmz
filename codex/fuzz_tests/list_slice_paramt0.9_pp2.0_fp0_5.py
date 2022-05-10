import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
b=a
print(len(weakref.getweakrefs(b)))
lst=lst*6
print(len(weakref.getweakrefs(b)))


lst=[1]*100000
del lst[1000:]
print(len(lst))
