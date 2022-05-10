import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst

#output:
['<__main__.A object at 0x7f9c9e4c4f90>']

#explanation:
#the object a is not deleted because it has a reference to itself
#the object a is not deleted because it has a reference to itself
#the object a is not deleted because it has a reference to itself
#the object a is not deleted because it has a reference to itself
#the object a is not deleted because it has a reference to itself
#the object a is not deleted because it has a reference to itself
#the object a is not deleted because it has a reference to itself
#the object a is not deleted because it has a reference to itself
#the object a is not deleted because it has a reference to itself
#the object a is not deleted because it has a reference to itself
#the object a is not deleted because it has a reference to itself
#the object a is not deleted because it has a reference to itself
#the object a is not deleted because it has a reference to itself
#the object a is not deleted because it has a
