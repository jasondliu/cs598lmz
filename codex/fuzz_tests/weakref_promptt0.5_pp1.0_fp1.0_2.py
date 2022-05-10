import weakref
# Test weakref.ref(self)

class A(object):
    def __init__(self):
        self.b = B(self)

class B(object):
    def __init__(self, a):
        self.a = weakref.ref(a)

a = A()
print a.b.a()
</code>
I got the following error:
<code>Traceback (most recent call last):
  File "weakref.py", line 12, in &lt;module&gt;
    print a.b.a()
TypeError: 'weakref' object is not callable
</code>
I have no idea why I got this error.


A:

You need to call the <code>weakref.ref</code> instance:
<code>print a.b.a()
</code>
should be
<code>print a.b.a
</code>

