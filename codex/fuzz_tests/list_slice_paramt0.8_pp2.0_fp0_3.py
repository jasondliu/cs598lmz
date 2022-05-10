import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
lst[0]=a
keepali0e.append(weakref.ref(lst[0],callback))
del a
del lst[0]
for i in xrange(100):del keepali0e[0]()
print 'done'
</code>
I don't know what is the reason for this. Please give me some advice.
Thank you very much!
My system:Python 2.6.4 on windows XP.


A:

I believe this is a Python bug, and should be reported as such. A couple of related links:

No segfault on Python 2.5, but segfault on 2.6: http://bugs.python.org/issue166645
Another reference to the same problem: http://code.google.com/p/modwsgi/issues/detail?id=25

The code below isn't my own, but I believe it's a nicely simplified version of the code you posted:
<code>import weakref,gc

class A(object):

    def __init__(self):
        self.c = self

def
