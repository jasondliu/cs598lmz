import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(weakref.ref(a,callback))
del a

print '   list len before gc:' + str(len(lst))
gc.collect()
time.sleep(1)
print 'list len after for gc:' + str(len(lst))
</code>

gc.collect() 之后 list 元素变化：

<code>   list len before gc:2
list len after for gc:1
</code>


A:

<code>callback</code> is called because it's on the callback list of the <code>ref</code> which is in the list. <code>a</code> is garbage because no other reference to it exists except for the reference held by the <code>ref</code> in the list. The callback is called at the next collection.

