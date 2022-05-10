import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(lst[:])
keepali0e.append(lst[:])
keepali0e.append(lst[0])
keepali0e.append(lst[0])
for i in keepali0e[:]:del keepali0e[0]
del lst
del a
del keepali0e
summary()
</code>
I expected to <code>lst</code>'s count is 0 but after <code>del lst</code> it's count is still appears as 1 and when I run
<code>lst=[str()]
lst[:]=[]
</code>
It's count still appears as 1.
and Also the same problem appear with
<code>del lst[0]
</code>
and then list <code>count</code> still appears as 1.
Why when I clear <code>lst</code> with <code>lst=[]</code> it's count is 0 and also when I
