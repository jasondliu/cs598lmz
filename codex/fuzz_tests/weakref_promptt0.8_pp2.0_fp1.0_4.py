import weakref
# Test weakref.ref
class C:
	def __init__(self, arg):
		self.arg = arg
	def __del__(self):
		print 'deleted', self.arg

a = C(10)
r = weakref.ref(a)
print r() is a
del a
print r() is None
print r()
assert r() is None

# Test weakref.WeakKeyDictionary()
class C:
	pass
a = C()
b = C()
c = C()
d = C()
d.x = a
d.y = b
w = weakref.WeakKeyDictionary()
w[c] = 1
w[d] = 2
print w.data
print w.data.keys()
del d, c
print w.data
print w.data.keys()
assert len(w.data.keys()) == 0

assert len(w.data) == 0

def get_key(k):
	print k()

w = weakref.WeakKeyDictionary()
a = C()
b = C()
w[
