import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.a=[keepalive]
b.c=callback
for i in xrange(20):
    lst.append(a)
xx=str()
for i in xrange(20):
    lst.append(b)
lst.pop(0)
xx=''
gc.collect()
for name in dir():del globals()[name]
assert all(lambda x:x==result,lst)
del lst
del callback
del gc.garbage[:]
del gc.garbage
gc.collect()
del xx
keepali0e=[]
gc.collect()
assert all(lambda x:x==result,list(dir()))
print test_result
</code>
This code runs in Cpython 2.6.8 and produces a multiple seg faults (at what appears to be seven crashes, about 25% of the time):
<code>$&gt;./python explo.py
&lt;class 'str'&gt;
&lt;type 'object'&gt;
&lt;type 'object'&gt;

