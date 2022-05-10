import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
def f():
    for i in xrange(1000000):
        a=A()
        a.c=lst[0]
        a.callback=callback
        weakref.ref(a,a.callback)
    print 'OK'
f()
</code>
The program crashed.
But if I use <code>str()</code> instead of <code>A()</code>, it runs OK.
What is the reason?


A:

I think I found the answer.
The weakref callback is called in the <code>del</code> statement. When <code>del a</code> is called, <code>a.callback</code> is called and then <code>a</code> is destroyed.
If <code>a</code> is an instance of <code>A</code>, <code>a.callback</code> is called and <code>a.c</code> is the <code>A</code> instance <code>a</code> itself, so <code>a</code> is not deleted, <code
