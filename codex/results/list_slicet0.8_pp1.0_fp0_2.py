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
This code works with <code>python 2.7</code>, but not with <code>python 3.4</code>. I have tested it in <code>IPython</code>, <code>Spyder</code> and <code>IDLE</code>.
I have also tried re-installing <code>python3</code> to <code>3.6</code>, but it still didn't work.
Why is this?

