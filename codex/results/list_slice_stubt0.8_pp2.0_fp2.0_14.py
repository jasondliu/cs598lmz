import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.lst=lst
keepali0e.append(a)
w=weakref.ref(a,callback)
print lst,callback
del a
print lst

print id(lst)    #output:140101052175968
print lst        #output:[]

print id(lst)
print lst

print id(keepali0e[0])
print keepali0e[0]
