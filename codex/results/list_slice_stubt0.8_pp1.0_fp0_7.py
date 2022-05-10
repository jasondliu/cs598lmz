import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
list1=weakref.WeakKeyDictionary({a:lst})
list2=weakref.WeakValueDictionary({a:lst})
list1[a].append(1)
list2[a].append(2)
del a
print(lst)
print(list1)
print(list2)
print()

a=A()
a.c=a
keepalive.append(a)
list3=weakref.WeakValueDictionary({a:lst})
list3[a].append(3)
del a
print(lst)
print(list1)
print(list2)
print(list3)
print()

a=A()
a.c=a
keepalive.append(a)
list4=weakref.WeakKeyDictionary({a:lst})
list4[a].append(4)
del a
print(lst)
print(list1)
print(list2)
print(list3)
print(list4)
