import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
del a
lst.append(weakref.ref(lst,callback))
del lst
keepalive.pop().c

#The following code is a simple example of a memory leak caused by circular references.
#The leak is caused by the fact that the list object has a reference to itself,
#and the list object has a reference to the object A.
#The object A has a reference to the list object.
#The list object has a reference to the object A.
#The object A has a reference to the list object.
#The list object has a reference to the object A.
#The object A has a reference to the list object.
#The list object has a reference to the object A.
#The object A has a reference to the list object.
#The list object has a reference to the object A.
#The object A has a reference to the list object.
#The list object has a reference to the object A.
#The object A has a reference to the list object.
#The list object has a reference to the object A
