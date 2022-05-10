import weakref
# Test weakref.ref
class G(object):

	def __init__(self):
		self.a = 1
a = G()
b = weakref.ref(a, lambda x: x)
a = None
print(b())
