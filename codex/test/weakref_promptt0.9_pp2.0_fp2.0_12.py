import weakref
# Test weakref.ref

def f(p):
    print('f() looses ref to', p)

class Example:
    def __del__(self):
        print('__del__ called on', self)

e = Example()
wref = weakref.ref(e, f)
print('ref returned by weakref.ref() is', wref)
print('e is weakly referenced by', wref() is e)

refobj = Example()
wr1 = weakref.ref(refobj, f)
print(wr1)
print(wr1())
wr2 = wr1()
print(wr2)

print('end')
wr1 = wr2 = None
print('end2')
refobj = None
print('end3')

e = wref = None
