import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
for i in range(10):
    lst.append(str())
</code>
So, I have a list that I don't want to collect by the garbage collector. But, I also want to remove the first element of the list, when the object A is destroyed.
This is the code I'm using for that, that I've tested and it works. 
But, I wanted to know if it was possible to do without the list. Now I don't need the list, but it can be the case I need it later. So, I want to know if this is possible. I tried using:
<code>weakref.ref(a,callback)
</code>
But it doesn't work. I'm pretty sure I read somewhere that it is possible to do with a weakref, but I can't find the article that proves that.
Now, I have already read that:
Collecting cycles in Python
but, it doesn't answer my question.


A:

It should work if you bind the callback to the <code>a.c</code> weak reference, because the callback is bound to the created weak reference
