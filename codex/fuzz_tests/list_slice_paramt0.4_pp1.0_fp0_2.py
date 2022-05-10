import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
lst

#Output:
#['<__main__.A object at 0x0000022D0A0C8A90>']

#The object is not deleted from the list.

#Now, let's try the same thing with a weakref.finalize object:

import weakref
class A(object):pass
lst=[str()]
a=A()
a.c=a
f=weakref.finalize(a,lambda x:del lst[0])
del a
lst

#Output:
#[]

#The object is deleted from the list.

#The following example is a little more complex.

#Here, we create two objects, a and b, and set the attribute c of a to b.
#Then we create a weakref.finalize object, f, for a and register a callback
#function. The callback function deletes the object a from the list lst.
#The finalize object, f, is then deleted.

#Now, we set the attribute c of b to a and delete the object b.
