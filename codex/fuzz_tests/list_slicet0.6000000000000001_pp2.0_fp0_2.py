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
</code>
I tried to run it in python3.3 and it told me that I can't call <code>del</code> on a list while iterating it.
I tried to run it in python2.7 and it didn't give me any error, but I'm not sure that it was right.
It seems to me that it should have given me an error in python2.7 too.
Am I right?
If yes, why does it work in python2.7?
If no, why does it give me an error in python3.3?

