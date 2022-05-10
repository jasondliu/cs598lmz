import gc, weakref

class A(object):
    def f(self):
        print 'A.f'

class B(object):
    def f(self):
        print 'B.f'

class C(A, B):
    pass

def f(a):
    a.f()

c = C()
ref = weakref.ref(c)
print type(ref)
print ref
print ref()
print ref() is c
print ref() is None

f(c)
print

del c
print ref() is None
print

gc.collect()
print ref() is None
</code>
The output is:
<code>&lt;type 'weakref'&gt;
&lt;weakref at 0x7f6bd332b6e8; to 'C' at 0x7f6bd332b0d0&gt;
&lt;__main__.C object at 0x7f6bd332b0d0&gt;
True
True
A.f

True

True
</code>
The <code>ref()</
