import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
lst.append(a)
keepali0e.append(weakref.ref(lst,callback))
del a,lst
t=1
while t:
    time.sleep(1)
    for i in keepali0e:
        r=i()
        if r is not None:
            print ('i is alilve')
        else:
             print ('i is dead~')
             t=0
    print ('next loop')
</code>
When it runs, the result is :
<code>i is alilve
i is alilve
next loop
i is alilve
i is dead~
next loop
</code>


A:

You just need to remove the <code>del lst[0]</code> statement and set <code>lst = None</code> after your other <code>del</code> statements. Here's proof that this works:
<code>import time
import weakref
class A(object):pass
def callback(x):lst = None #del lst[0]
keepali0e=[]
