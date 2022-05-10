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
I have tried to run it in python 2.7 and 3.3, but it doesn't work.
I have also tried to run it in pypy, but it doesn't work.
I have also tried to run it in python 2.7 with <code>-X faulthandler</code>, but it doesn't work.
I have also tried to run it in python 2.7 with <code>-X tracemalloc</code>, but it doesn't work.
I have also tried to run it in python 2.7 with <code>-X gc</code>, but it doesn't work.
I have also tried to run it in python 2.7 with <code>-X gc -X faulthandler -X tracemalloc</code>, but it doesn't work.
I have also tried to run it in python 2.7 with <code>-X gc -X faulthandler -X tracemalloc -X trackrefs</code>, but it doesn't work.
I have also tried to run it in python 2.7 with <code>-X gc -X
