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
This is the first time I've ever seen this problem.
I've tried a variety of fixes, but the best I could do was remove the <code>del a</code> line, and then the problem would go away.
I've also tried to remove the <code>del lst[0]</code> line and the problem would go away.
I've also tried to remove the <code>lst=[str()]</code> line and the problem would go away.
I've also tried to remove the <code>str()</code> call and the problem would go away.
I've also tried to use the <code>list()</code> function instead of the <code>[]</code> syntax and the problem would go away.
I've also tried to remove the <code>keepali0e.append(lst[:])</code> line and the problem would go away.
I've also tried to remove the <code>keepali0e.append(weakref.ref(a,callback))</code> line and the problem would go away.
I've also tried to remove the <code>a.c=
