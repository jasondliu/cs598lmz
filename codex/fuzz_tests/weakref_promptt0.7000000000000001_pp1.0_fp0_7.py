import weakref
# Test weakref.ref(method)
# with this class
class A(object):
    def __init__(self):
        self.test = 1
    def foo(self):
        return self.test
a = A()
a_ref = weakref.ref(a)
f_ref = weakref.ref(a.foo)
print(f_ref())
a.test = 10
print(f_ref())
del a
print(a_ref())
print(f_ref())
</code>
It prints:
<code>1
10
None
10
</code>
It seems <code>f_ref</code> is not bound to <code>a</code>.
What is the reason?

