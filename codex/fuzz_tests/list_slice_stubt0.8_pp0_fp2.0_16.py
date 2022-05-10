import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
p=weakref.proxy(a,callback)
keepali0e.append(p)
b=p.c
c=b.c
d=c.c
print len(lst)
</code>
The <code>a</code> object refers to <code>a</code> itself, and the proxy refers to <code>a</code>. It seems that the reference counter of <code>a</code> will increase. According to the source code, <code>a</code> will not be deleted until the end because the reference count is more than 1. 
Why is <code>lst</code> deleted in this case?


A:

First, Python objects do not have reference counts. Rather, they have a reference graph rooted at the remaining names, and this graph is traversed to find possible circular references, which then keep objects alive.
Second, proxies do not hold a reference to the target, instead they hold a special reference that tracks cycles internally. This means that even if the proxy is only reachable via a circular reference, the proxy does not make a cycle in the graph.
So the <code>keepalive</
