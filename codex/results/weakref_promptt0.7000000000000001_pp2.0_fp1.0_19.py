import weakref
# Test weakref.ref(obj)
obj = [1,2,3]
r = weakref.ref(obj)
print r().pop()
print r()
print obj

class Foo(object):
	def __init__(self):
		print 'created'

# Test weakref.WeakKeyDictionary
class wkdict(object):
	def __init__(self):
		self.dict = weakref.WeakKeyDictionary()

	def test(self):
		f = Foo()
		self.dict[f] = 'test'
		print self.dict
		f.test()
		f = None
		print self.dict

# Test weakref.WeakValueDictionary
class wvdict(object):
	def __init__(self):
		self.dict = weakref.WeakValueDictionary()

	def test(self):
		f = Foo()
		self.dict[f] = 'test'
		print self.dict
		f.test()
		f = None
		print self.dict


