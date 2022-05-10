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
print(len(keepali0e))
</code>
the code above will print <code>2</code>
but when I change the last line to:
<code>while lst:keepali0e.append(lst[:])
</code>
the code above will print <code>3</code>
I know that when we call <code>lst[:]</code> it will create a new list and append it to the list <code>keepali0e</code> and create a new reference to the object <code>a</code> which will prevent it from being deleted.
but I still don't understand why it's different from <code>lst[0]</code>
in my mind, the <code>lst[:]</code> will create a shallow copy, just like <code>lst[0]</code>
can anyone explain it to me?


A:

<code>lst[:]</code> creates a new list that refers to the same objects as <code>lst</code>.  If you do <code>lst[:]</code> inside a <code
