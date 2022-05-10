import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
del a.c
del keepali0e
print lst,lst[0]
lst=[]
lst.append("asdf")
lst.append("asdf")
lst.append("asdf")
lst.append("asdf")
print lst
lst.remove("asdf")
print lst

#print dir(lst)
print lst.count("asdf")
lst.insert(0,"asdf")
print lst
lst.reverse()
print lst
lst.sort()
print lst
lst.extend(["asdf","asdf","asdf"])
print lst
print lst.index("asdf")
lst.pop()
print lst
print lst.pop(0)
print lst
