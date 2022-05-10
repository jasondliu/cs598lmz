import weakref
# Test weakref.ref() on a function.
def f():
    pass


wf = weakref.ref(f)
f is None
f()
f is wf()
f is None
f is None
wf() is None
# Test weakref.ref() on a method.
class A:

    def f(self):
        pass


a = A()
wa = weakref.ref(a.f)
a.f is None
a.f()
a.f is wa()
a.f is None
a.f is None
wa() is None
# Test weakref.ref() on a builtin method.
wb = weakref.ref(int.to_bytes)
int.to_bytes is None
int.to_bytes(1, 2)
int.to_bytes is wb()
int.to_bytes is None
int.to_bytes is None
wb() is None
# Test weakref.ref() on a builtin function.
wb = weakref.ref(len)
len is None
len([])
len is wb()
len is None
len is None

