import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(lst,callback))
</code>
I expect that when I delete the a object, <code>callback</code> function will be called and  can be called normally by operating <code>weakref.ref</code>, but this test always seems to be blocked in Python3, there is nothing in pythn2.

If I create a class in Python3, and then use <code>weakref.ref</code> to create an alias, it will also block, for example:
<code>class A(object):
    def __init__(self):
        self.cyclic=self
def callback(x):
    del lst[0]
lst=[str()]
keepali0e=[]
a=A()
a.cyclic=a
keepali0e.append(weakref.ref(lst,callback))
</code>

If you modify the last code to:
<code>class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.cyclic=a
keep
