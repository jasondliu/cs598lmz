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
The first use case is not so useful by itself, but sometimes when dealing with 3rd party libraries, this is the only way to keep a reference to a piece of data (e.g. <code>a.c</code>) that may go away whenever the object (<code>a</code>) or the class (<code>A</code>) is deleted. The second use case is more useful, but the idea is the same, you have some data that is hard to keep track of, so you keep a reference to it, and then use this reference to access the data.
Please note, that for the second case, there is an alternative way, by creating an instance of a class that has a method returning the desired data, and then appending the instance to the list, like as follows:
<code>import weakref
class B(object):
    def __init__(self,x): self.x=x
    def get(self): return self.x

class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
b=B
