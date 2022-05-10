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
That being said, I have a number of questions:

Is there a better way to do this?
If not, is there a way to make the program more efficient?
If not, is there a way to make the program more readable?
Is there a way to make the program more reliable?


