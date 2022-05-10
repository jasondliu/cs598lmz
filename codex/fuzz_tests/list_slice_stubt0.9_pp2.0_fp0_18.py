import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(lst)
keepalive.append(a)
wr=weakref.ref(lst[0],callback)
</code>
This snippet does not give me any segfault or memory leaks,while the other example would segfault immediately with a <code>Blob</code> added to the <code>list</code>.What is happening here is the loop the <code>str</code> makes and the <code>list</code> makes is creating a cycle before the <code>str</code> <code>__del__</code> gets called and breaks things(I also know <code>str</code> doesn't have a <code>__del__</code> method but this is just pseudo-code).
So my question is how to do the same thing in c++.How do I point a c++ object to itself and then delete it safely?
For those that want to know the full story,I stumbled upon this accidentally while looking at the module <code>_PyWeakref_RefType</code> in cpython and how it triggered the <code>__del__</code> method:

