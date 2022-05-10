import weakref
# Test weakref.ref(weakref.ref(x)) == weakref.ref(x)

class A:
    pass

def test(x):
    r = weakref.ref(x)
    rr = weakref.ref(r)
    return rr() is r

a = A()
print(test(a))
print(test(A()))
print(test(A))
print(test(A()))
print(test(A))
print(test(A()))
print(test(A))
print(test(A()))
print(test(A))
print(test(A()))
print(test(A))
print(test(A()))
print(test(A))
print(test(A()))
print(test(A))
print(test(A()))
print(test(A))
print(test(A()))
print(test(A))
print(test(A()))
print(test(A))
print(test(A()))
print(test(A))
print(test(A()))
print(test(A))
