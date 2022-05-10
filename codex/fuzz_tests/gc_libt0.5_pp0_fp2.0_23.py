import gc, weakref

def get_refcounts(objects):
    return dict([(id(o), sys.getrefcount(o)) for o in objects])

class A:
    pass

a = A()
b = A()

a_id = id(a)
b_id = id(b)

refcounts = get_refcounts([a, b])

print('a:', sys.getrefcount(a))
print('b:', sys.getrefcount(b))

print('a_id:', a_id)
print('b_id:', b_id)

print('refcounts:', refcounts)

print('a:', a)
print('b:', b)

print('a.__class__:', a.__class__)
print('b.__class__:', b.__class__)

print('a.__class__.__class__:', a.__class__.__class__)
print('b.__class__.__class__:', b.__class__.__class__)

