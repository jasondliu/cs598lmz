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
print len(lst)
</code>
I would expect the output to be 0, but it is 1.
What is the correct way to remove the last item from the list?

