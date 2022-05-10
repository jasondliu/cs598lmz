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
print len(keepali0e)
</code>
I get the following output:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "&lt;stdin&gt;", line 12, in &lt;module&gt;
RuntimeError: maximum recursion depth exceeded
</code>
If I remove the line <code>a.c=a</code> the program runs to completion.
Is there a way to avoid this error?


A:

I'm not sure why you're getting a recursion error, but you can avoid it by using <code>weakref.finalize</code> instead of a callback:
<code>import weakref

class A(object):
    pass

def callback(x):
    del lst[0]

keepali0e = []
lst = [str()]
a = A()
a.c = a
keepali0e.append(weakref.finalize(a, callback))
del a

while lst:
