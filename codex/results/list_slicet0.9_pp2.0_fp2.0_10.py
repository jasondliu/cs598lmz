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
print len(keepali0e)
</code>
First I thought it comes from my age, then from my backache, then from my eyes... It turns out it's not from my backache but from the code !
Everytime it runs about 8k MB of swap is used, so I did the code above.
Is there anything I am missing ?


A:

I got the answer on the python-talk mailing list.
What I am missing is : the garbage is not part of a compact cycle.

