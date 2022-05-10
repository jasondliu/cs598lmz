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
lst.append(str())
</code>
This will have the interpreter crash, perhaps not giving you a traceback.
The <code>while</code> loop is there to ensure that all the references in <code>keepali0e</code> are really alive.


A:

I think this is a bug/limitation of CPython. There is a circular reference, which should be handled. 
The following code is able to crash the interpreter:
<code>import sys
import weakref

# Hard reference to the list
l = []

# Deletion function
def delete(x):
    del l[0]

# Adding an object with a reference to itself
a = A()
a.c = a

# Creating a weakref from the object
weakref.ref(a, delete)
del a

# Adding objects to the list to keep all references alive
for i in range(10):
    l.append(object())

# Deleting the first element in the list
# This should fire the deletion function
del l[0]

# Print the reference count of the list

