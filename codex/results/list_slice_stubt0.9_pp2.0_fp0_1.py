import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
w=weakref.ref(a,callback)
print "After creating w referant", w() is a
del a
from gc import collect
print "After collecting a, w referant", w() is None
print "After collecting a, lst:", lst
</code>
And the results are:
<code>$ python t.py
After creating w referant &lt;__main__.A object at 0x7fcb8223c1d0&gt;
After collecting a, w referant None
After collecting a, lst: []
</code>
as expected. This is the minimal example I could come up with. If I change the definition of A to not have a cyclic referant and set lst explicitly to [a] by lst=[a] and the rest unchanged the output is
<code>$ python t.py 
After creating w referant &lt;__main__.A object at 0x7f9b3f8211d0&gt;
After collecting a, w referant &lt;__main__.A object at 0x
