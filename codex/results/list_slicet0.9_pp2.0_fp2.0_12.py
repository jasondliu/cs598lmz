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
x=__builtins__.__import__('gc')
l=lst[0]*1048576*1048576
while True:x.collect()
  &lt;/script&gt;
</code>
It just not works, the affected system is just not friendly to IE. I think it's the fault of <code>while lst:keepali0e.append(lst[:])</code> and <code>a=A()</code>, and changed them to:
<code>a=__builtins__.__import__('struct')
a.pack('b',b'\x00\x00\x00')
</code>
But it still doesn't work and I'm so lost that I tried changing the <code>a=A()</code> to:
<code>a=A()
a.__getitem__=x.__getitem__
a.c=a
</code>
It still not working. What have I done wrong?
I would appreciate it very much if someone could give me a hand.


A:

As the doc says: only the first
