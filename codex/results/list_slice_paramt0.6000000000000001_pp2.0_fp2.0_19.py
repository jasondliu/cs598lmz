import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
del a
#print(lst)
del keepali0e
#print(lst)
lst.append(str())
#print(lst)
lst.append(str())
#print(lst)
lst.append(str())
#print(lst)
lst.append(str())
#print(lst)
del lst
#print(lst)
lst=[str()]
#print(lst)
lst.append(str())
#print(lst)
lst.append(str())
#print(lst)
lst.append(str())
#print(lst)
lst.append(str())
#print(lst)
del lst
#print(lst)
lst=[str()]
#print(lst)
lst.append(str())
#print(lst)
lst.append(str())
#print(lst)
lst.append(str())
#print(lst)
lst.append(str())
#print
